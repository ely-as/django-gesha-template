from django.db import models
from django.utils.translation import gettext_lazy as _


class Enquiry(models.Model):
    name = models.CharField(_("Name"), max_length=255)
    email = models.EmailField(_("Email address"))
    phone_number = models.CharField(_("Phone number"), max_length=17)
    description = models.TextField(_("Description"))
