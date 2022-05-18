from django.contrib import admin
from .models import Data, DataB

# Register your models here.
class DataAdmin(admin.ModelAdmin):
    list_display = ('nitrogen', 'phosphorus', 'potassium', 'temperature', 'humidity', 'ph', 'rainfall', 'predicted_crop')

admin.site.register(Data, DataAdmin)

class DataAdminB(admin.ModelAdmin):
    list_display = ('crop', 'predicted_conditions')

admin.site.register(DataB, DataAdminB)