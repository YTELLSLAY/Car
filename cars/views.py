from django.shortcuts import render
from .models import Car
from .form import formulario



def cars_view(request):
    car = Car.objects.all()
    search = request.GET.get('search')

    if search:
        car = Car.objects.filter(model__contains=search)
    return render(request, 'cars.html', {'car' : car})

def form_views(request):
    form = formulario()
    return render(request, 'car_form.html', {'form':form})