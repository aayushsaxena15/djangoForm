from django.contrib import admin

# Register your models here.
from .models import Station, Cluster, Strategy

admin.site.register(Station)
admin.site.register(Cluster)
admin.site.register(Strategy)