import gesha
from django.views.generic import TemplateView


class IndexView(gesha.JSContextMixin, TemplateView):
    template_name = "{{ project_name }}_app/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        projname = "{{ project_name }}"
        context["script_path"] = f"{projname}_app/dist/{projname}.bundle.min.js"
        context["stylesheet_path"] = f"{projname}_app/dist/main.css"
        return context
