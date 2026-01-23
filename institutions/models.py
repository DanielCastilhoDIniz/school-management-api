from django.db import models
from django.utils.translation import gettext_lazy as _
from core.models.base import Base
from core.models.address import Address




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





