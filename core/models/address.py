from django.db import models
from django.db import IntegrityError

from django_countries.fields import CountryField

from django.utils.translation import gettext_lazy as _
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

from django.core.validators import MinLengthValidator, BaseValidator
from django.core.exceptions import ValidationError


import re

from core.models.base import Base



class BrazilianZipCodeValidator(BaseValidator):
    message = _("Formato de CEP inválido para o Brasil. Use: 00000-000")
    code = 'invalid_brazilian_zip'

    def __init__(self, message=None):
        super().__init__(limit_value=None, message=message)

    def __call__(self, value):
        if not value: return
        # Apenas números para validar a extensão
        numbers_only = re.sub(r'\D', '', str(value))
        if len(numbers_only) != 8:
            raise ValidationError(self.message, code=self.code)

    @staticmethod
    def clean(value):
        numbers_only = re.sub(r'\D', '', str(value))
        return f"{numbers_only[:5]}-{numbers_only[5:]}" if len(numbers_only) == 8 else value


class BrazilianStateValidator(BaseValidator):
    """
    Validador para siglas de estados brasileiros
    """
    message = _("Invalid Brazilian state abbreviation")
    code = 'invalid_brazilian_state'

    BRAZILIAN_STATES = {
        'AC', 'AL', 'AP', 'AM', 'BA', 'CE', 'DF', 'ES', 'GO',
        'MA', 'MT', 'MS', 'MG', 'PA', 'PB', 'PR', 'PE', 'PI',
        'RJ', 'RN', 'RS', 'RO', 'RR', 'SC', 'SP', 'SE', 'TO'
    }

    def __call__(self, value):
        if not value:
            return

        value = str(value).strip().upper()

        if value not in self.BRAZILIAN_STATES:
            raise ValidationError(self.message, code=self.code)
    @staticmethod
    def clean(value):
        """normalize UPPERCASE"""
        return str(value).strip().upper()

class Address(Base):
    """
    address model
    """
    # ── Generic Foreign Key (allows you to associate it with ANY model.)
    content_type = models.ForeignKey(
        ContentType,
        on_delete=models.CASCADE,
        verbose_name=_("Owner Type"),
        related_name="addresses",           # allows: obj.addresses.all()
        help_text=_("Type of the object that owns this phone (e.g., Student, Teacher, Institution)"),
        )
    # it's possible to change PositiveBigIntegerField for Charfield - it might break here
    object_id = models.PositiveBigIntegerField(
        verbose_name=_("Owner ID"),
        help_text=_("ID of the object that owns this address"),
        )

    content_object = GenericForeignKey(
        ct_field="content_type",
        fk_field="object_id",
        )

    # address type
    class AddressesTypeChoices(models.TextChoices):
        HOME = 'home', _('Home')
        WORK = 'work', _('Work')
        BILLING = 'billing', _('Billing')
        SHIPPING = 'shipping', _('Shipping')
        OTHER = 'other', _('Other')

    address_type = models.CharField(
        max_length=25,
        verbose_name=_("address type"),
        choices=AddressesTypeChoices.choices,
        default=AddressesTypeChoices.HOME,
        help_text=_("Purpose of this address")
        )

    is_primary = models.BooleanField(
        default=False,
        verbose_name=_("Primary address"),
        help_text=_("Is this the primary address for this owner?"),
        )

    # ── Address Details
    country = CountryField(
        verbose_name=_("country"),
        default= "BR",
        blank_label=_("Select a country")
        )
    state = models.CharField(
        max_length=100,
        verbose_name=_("state")
        )
    city = models.CharField(
        max_length=100,
        verbose_name=_("city")
        )
    district = models.CharField(
        max_length=100,
        verbose_name=_("district"),
        help_text=_("Neighborhood or district name"),
        )
    street = models.CharField(
        max_length=200,
        verbose_name=_("street"),
        validators=[MinLengthValidator(3)],
        help_text=_("Street name and number"),
        )
    number = models.CharField(
        max_length=10,
        verbose_name=_("number"),
        default='S/N',
        help_text=_("Building/house number. Use 'S/N' for no number"),
        )
    complement = models.CharField(
        max_length=100,
        blank=True,
        verbose_name=_("complement"),
        help_text=_("Apartment, floor, block, etc.")
        )
    zip_code = models.CharField(
        max_length=15,
        verbose_name=_("zip code"),
        help_text=_("ZIP code"),
        )

    class Meta:
        verbose_name = _("Address")
        verbose_name_plural = _("Addresses")
        ordering = ["-is_primary", "city", "street"]
        db_table = "address"

        constraints = [
            models.UniqueConstraint(
                fields=['content_type', 'object_id'],
                condition=models.Q(is_primary=True),
                name='unique_primary_address_per_owner'
            ),
        ]

        indexes = [
            models.Index(fields=['content_type', 'object_id']),
            models.Index(fields=['zip_code']),
            models.Index(fields=['city', 'state']),
            models.Index(fields=['is_primary']),
        ]

    # Methods

    def clean(self):
        """Validations and standardizations"""
        errors = {}

        # standardization fields
        if self.street:
            self.street = self.street.strip()

        if self.city:
            self.city = self.city.strip()

        if self.district:
            self.district = self.district.strip()

        if self.state:
            self.state = self.state.strip()

        if self.country == 'BR':
            zip_validator = BrazilianZipCodeValidator()
            try:
                zip_validator(self.zip_code)
                self.zip_code = zip_validator.clean(self.zip_code)
            except ValidationError as e:
                errors['zip_code'] = str(e)  # or e.message

            state_validator = BrazilianStateValidator()
            try:
                state_validator(self.state)
                self.state = state_validator.clean(self.state)
            except ValidationError as e:
                errors['state'] = str(e)

        # Number validation (more flexible)
        if self.number and self.number.upper() != 'S/N':
            if not any(c.isdigit() for c in self.number):
                errors['number'] = _(
                    "House number should contain at least one digit unless it's 'S/N'."
                )

        if errors:
            raise ValidationError(errors)


    def save(self, *args, **kwargs):
        """
        Ensure all validations are performed before saving.
        """
        self.full_clean()
        if self.is_primary:
            Address.objects.filter(
                content_type=self.content_type,
                object_id=self.object_id,
                is_primary=True
            ).exclude(pk=self.pk).update(is_primary=False)
        try:
            super().save(*args, **kwargs)
        except IntegrityError as e:
            if 'unique_primary_address_per_owner' in str(e):
                raise ValidationError({
                    'is_primary': _("There is already a primary address for this owner.")
                })
            raise

    def __str__(self):
        primary = "★ " if self.is_primary else ""
        return f"{primary}{self.street}, {self.number} - {self.city}/{self.state}"

    # Utilitarian properties
    @property
    def full_address(self):
        parts = []

        # Street and number
        street = (self.street or "").strip()
        number = (self.number or "").strip()
        if street:
            if number and number.upper() != "S/N":
                parts.append(f"{street}, {number}")
            else:
                parts.append(street)

        # Complement and district
        if self.complement:
            parts.append(self.complement)
        if self.district:
            parts.append(self.district)

        # City - State
        city_state = [part for part in [(self.city or "").strip(), (self.state or "").strip()] if part]
        if city_state:
            parts.append(" - ".join(city_state))

        # ZIP code
        if self.zip_code:
            parts.append(self.zip_code)  # já formatado pelo clean()

        # Country (only if not Brazil)
        if self.country.code != 'BR':
            parts.append(str(self.country.name))

        return ", ".join(parts)


    def set_as_primary(self):
        """Define este endereço como primário"""
        # Remove primary de outros endereços do mesmo owner
        Address.objects.filter(
            content_type=self.content_type,
            object_id=self.object_id,
            is_primary=True
        ).update(is_primary=False)

        self.is_primary = True
        self.save(update_fields=['is_primary'])