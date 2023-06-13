import gesha
from django.http import HttpRequest, JsonResponse
from django.views import View
from django.views.generic import TemplateView

from {{ project_name }}_app import forms


class IndexView(gesha.JSContextMixin, TemplateView):
    template_name = "{{ project_name }}_app/index.html"

    def get_allowed_url_patterns(self):
        return ["enquiry"]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        projname = "{{ project_name }}"
        context["script_path"] = f"{projname}_app/dist/main.bundle.min.js"
        context["stylesheet_path"] = f"{projname}_app/dist/main.css"
        context["enquiry_form"] = forms.EnquiryForm()
        return context


class EnquiryView(View):
    def post(self, request: HttpRequest, *args, **kwargs) -> JsonResponse:
        form = forms.EnquiryForm(data=request.POST)
        if is_valid := form.is_valid():
            form.save()
        form_dict = {"is_valid": is_valid, "as_p": form.as_p()}
        return JsonResponse({"form": form_dict})
