import django_tables2 as tables
from . import models

class ReporterTable(tables.Table):
    class Meta:
        model = models.Coord_Reporter 