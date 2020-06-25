from cms.models.pluginmodel import CMSPlugin
from django.db import models

class Datatable(CMSPlugin):
    url = models.URLField(max_length=300)
    columns = models.CharField(max_length=1000, default='None')