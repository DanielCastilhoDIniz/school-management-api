from django.db import models
from django.utils.translation import gettext_lazy as _


class Base(models.Model):

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        abstract = True

# colocar no core
class Address(Base):
    """
    address model
    """
    street = models.CharField(max_length=200, verbose_name=_("street"))
    number = models.CharField(max_length=10, verbose_name=_("number"))
    complement = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        verbose_name=_("complement")
    )
    district = models.CharField(max_length=100, verbose_name=_("district"))
    city = models.CharField(max_length=100, verbose_name=_("city"))
    state = models.CharField(max_length=2, verbose_name=_("state"))
    zip_code = models.CharField(max_length=9, verbose_name=_("zip code"))
    country = models.CharField(max_length=50, verbose_name=_("country"),
                                default=_("Brasil"))

    class Meta:
        verbose_name = _("Address")
        verbose_name_plural = _("Addresses")
        ordering = ["city", "street"]
        db_table = "address"


    def __str__(self):
        return f'{self.street}, {self.number} - {self.city}/{self.state}'
# colocar no core
class Phone(Base):

    """
    phone model
    """

    class PhoneTypeChoices(models.TextChoices):
        MOBILE = 'mobile', _('Celular')
        LANDLINE = 'landline', _('Fixo')
        WHATSAPP = 'whatsapp', _('WhatsApp')

    number = models.CharField(max_length=20)
    type = models.CharField(
        max_length=10,
        choices=PhoneTypeChoices.choices,
        default=PhoneTypeChoices.MOBILE
        )

    institution = models.ForeignKey(
        'institutions.Institution',
        on_delete=models.CASCADE,
        related_name='phones'
    )

    class Meta:
        verbose_name = _("Phone")
        verbose_name_plural = _("Phones")
        ordering = ["type"]
        db_table = "phone"

    def __str__(self):
        return f'{self.number} ({self.type})'


class InstitutionType(Base):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Institution Type")
        verbose_name_plural = _("Institution Types")
        ordering = ["name"]
        db_table = "institution_type"


class Institution(Base):

    legal_name = models.CharField(max_length=100, verbose_name=_("legal_name"))
    trade_name = models.CharField(max_length=100, verbose_name=_("trade_name"))
    tax_identification_number = models.CharField(
        max_length=14,
        unique=True,
        verbose_name=_("tax identification number"))
    foundation_date= models.DateField(
        blank=True,
        null=True,
        verbose_name=_("foundation_date"))
    institution_type = models.ForeignKey(
        InstitutionType,
        related_name='institutions',
        verbose_name=_("institution_type"),
        on_delete=models.PROTECT)
    address = models.OneToOneField(
        Address,
        related_name='institution',
        on_delete=models.CASCADE,
        verbose_name=_('address'))

    email = models.EmailField(verbose_name=_("email"))
    website = models.URLField(
        verbose_name=_("website"),
        max_length=200,
        blank=True,
        null=True)
    description = models.TextField(
        verbose_name=_("description"),
        blank=True,
        null=True)

    def __str__(self):
        return self.legal_name

    class Meta:
        verbose_name = _("Institution")
        verbose_name_plural = _("Institutions")
        ordering = ['legal_name']
        db_table = 'institution'





