from django.contrib import admin
from cars.models import Car
from cars.models import Brand 


class CarAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    
admin.site.register(Brand, CarAdmin)



class AdminCar(admin.ModelAdmin):
    list_display = ('model', 'brand', 'factory_year', 'model_year', 'value', 'photo', )
    search_fields = ('model',)
    
admin.site.register(Car, AdminCar)