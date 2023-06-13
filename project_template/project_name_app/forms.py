from django import forms

from {{ project_name }}_app import models


class EnquiryForm(forms.ModelForm):
    class Meta:
        model = models.Enquiry
        fields = ["name", "email", "phone_number", "description"]
