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

def search_results(request):

    if 'image' in request.GET and request.GET["image"]:
        search_term = request.GET.get("image")
        searched_articles = Image.search_by_name(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"articles": searched_articles})

    else:
        message = "You havent searched for any term"
        return render(request, 'search.html',{"message":message})

def view_location(request, location):
    locations = Image.objects.distinct().values_list('location__name', flat=True)
    categories = Image.objects.distinct().values_list('category__name', flat=True)
    image = Image.objects.filter(location__name=location)
    return render(request, 'category.html', {"image": image, "locations": locations, 'categories': categories})




    