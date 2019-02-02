from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from cms.models.pluginmodel import CMSPlugin
from django.utils.translation import ugettext_lazy as _
from .models import Datatable

@plugin_pool.register_plugin
class DataTablePlugin(CMSPluginBase):
    model = Datatable
    name = _("Datatable")
    render_template = "datatable.html"
    cache = True

    def render(self, context, instance, placeholder):
        context = super(DataTablePlugin, self).render(context, instance, placeholder)
        return context
