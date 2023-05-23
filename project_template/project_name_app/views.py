import gesha
from django.views.generic import TemplateView


class IndexView(gesha.JSContextMixin, TemplateView):
    template_name = "{{ project_name }}_app/index.html"
