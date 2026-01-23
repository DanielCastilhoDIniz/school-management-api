from django.db import models
from django.utils.translation import gettext_lazy as _


from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.core.validators import RegexValidator

from core.models.base import Base


class Phone(Base):

    """
    Generic phone that could belong to any model.
    (ex: Institution, Student, Teacher, Employee, Guardian, etc.)
    """

    # validator for phone numbers
    phone_regex = RegexValidator(
    regex=r'^\+?1?\d{9,15}$',
    message=_("Phone number must be entered in the format:"
    " '+999999999'. Up to 15 digits allowed.")
    )

    # ── Generic Foreign Key (allows you to associate it with ANY model.)
    content_type = models.ForeignKey(
        ContentType,
        on_delete=models.CASCADE,
        verbose_name=_("Owner Type"),
        related_name="phones",           # allows: obj.phones.all()
        help_text=_("Type of the object that owns this phone (e.g., Student, Teacher)"),
    )
    # it's possible to change PositiveBigIntegerField for Charfield - it might break  here
    object_id = models.PositiveBigIntegerField(
        verbose_name=_("Owner ID"),
        help_text=_("ID of the object that owns this phone"),
    )

    content_object = GenericForeignKey(
        ct_field="content_type",
        fk_field="object_id",
    )

     # ── Phone Details
    number = models.CharField(
        max_length=20,
        verbose_name=_("number"),
        validators=[phone_regex],
        help_text=_("Ex: (11) 98765-4321, +5511987654321, etc.")
    )

    class PhoneTypeChoices(models.TextChoices):
        MOBILE = 'mobile', _('mobile')
        LANDLINE = 'landline', _('landline')
        WHATSAPP = 'whatsapp', _('WhatsApp')
        OTHER = 'other', _("other")

    type_phone = models.CharField(
        max_length=20,
        verbose_name=_("type phone"),
        help_text=_("Type of phone number"),
        choices=PhoneTypeChoices.choices,
        default=PhoneTypeChoices.MOBILE
    )

    is_main = models.BooleanField(
        default=False,
        verbose_name=_("Is this the main phone?"),
    )

    # ── Meta ────────────────────────────
    class Meta:
        verbose_name = _("Phone")
        verbose_name_plural = _("Phones")
        ordering = ["is_main","type_phone"]
        db_table = "phone"

        constraints = [
        models.UniqueConstraint(
            fields=['content_type', 'object_id', 'number'],
            name='unique_phone_per_owner'
        ),
        models.UniqueConstraint(
            fields=['content_type', 'object_id'],
            condition=models.Q(is_main=True),
            name='unique_main_phone_per_owner'
        ),
        ]

        # Ensures there are no duplicates of the same number for the same owner.
        unique_together = [['content_type', 'object_id', 'number']]

        # Index for quick searches
        indexes = [
            models.Index(fields=['content_type', 'object_id']),
            models.Index(fields=['number']),
        ]

    # Methods

    @property
    def clean_number(self):
        """Remove all non-numeric characters from the phone number"""
        import re
        return re.sub(r'\D', '', self.number)


    def __str__(self):
        owner = self.content_object
        owner_str = str(owner) if owner else _("No owner")
        type_display = self.get_type_display()
        main = " ★" if self.is_main else ""

        return f"{self.number} ({type_display}){main} – {owner_str}"

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)
