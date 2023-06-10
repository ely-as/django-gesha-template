from django.contrib import admin

from {{ project_name }}_app import models

admin.site.register(models.Enquiry)
