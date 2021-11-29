from django.shortcuts import render
from .models import Category, Image, Location

# Create your views here.
def images(request):
    location = request.GET.get('location')
    print('location:', location)

    categories = Category.objects.all()
    locations = Location.objects.all()
    photos = Image.objects.all()

    context = {'categories': categories, 'photos': photos, 'locations': locations}
    return render(request,'photos.html', context)