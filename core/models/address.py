from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType


from core.models.base import Base

class Address(Base):
    """
    address model
    """

    # ── Generic Foreign Key (allows you to associate it with ANY model.)
    content_type = models.ForeignKey(
        ContentType,
        on_delete=models.CASCADE,
        verbose_name=_("Owner Type"),
        related_name="addresses",           # allows: obj.phones.all()
        help_text=_("Type of the object that owns this phone (e.g., Student, Teacher, Institution)"),
    )
    # it's possible to change PositiveBigIntegerField for Charfield - it might break  here
    object_id = models.CharField(
        verbose_name=_("Owner ID"),
        help_text=_("ID of the object that owns this address"),
    )

    content_object = GenericForeignKey(
        ct_field="content_type",
        fk_field="object_id",
    )

    # ── Address Details
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

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)