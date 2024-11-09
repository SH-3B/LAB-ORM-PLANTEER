# plants/views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import Plant
from django.core.paginator import Paginator
from .forms import PlantForm

def all_plants(request):
    plants_list = Plant.objects.all()
    category_filter = request.GET.get('category')
    is_edible_filter = request.GET.get('is_edible')

    if category_filter:
        plants_list = plants_list.filter(category=category_filter)

    if is_edible_filter:
        plants_list = plants_list.filter(is_edible=True if is_edible_filter == 'true' else False)

    # Pagination: show 9 plants per page
    paginator = Paginator(plants_list, 9)
    page_number = request.GET.get('page')
    plants_page = paginator.get_page(page_number)

    return render(request, 'plant/all_plants.html', {
        'plants': plants_page,
        'category_filter': category_filter,
        'is_edible_filter': is_edible_filter
    })


def plant_detail(request, plant_id):
    plant = get_object_or_404(Plant, pk=plant_id)
    # Fetch related plants based on category
    related_plants = Plant.objects.filter(category=plant.category).exclude(id=plant.id)[:4]
    
    return render(request, 'plant/plant_detail.html', {'plant': plant, 'related_plants': related_plants})


def add_plant(request):
    if request.method == 'POST':
        form = PlantForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('plant:all_plants')
    else:
        form = PlantForm()
    
    return render(request, 'plant/add_plant.html', {'form': form})


def update_plant(request, plant_id):
    plant = get_object_or_404(Plant, pk=plant_id)
    if request.method == 'POST':
        form = PlantForm(request.POST, request.FILES, instance=plant)
        if form.is_valid():
            form.save()
            return redirect('plant:plant_detail', plant_id=plant.id)
    else:
        form = PlantForm(instance=plant)

    return render(request, 'plant/update_plant.html', {'form': form, 'plant': plant})


def delete_plant(request, plant_id):
    plant = get_object_or_404(Plant, pk=plant_id)
    if request.method == 'POST':
        plant.delete()
        return redirect('plant:all_plant')
    return render(request, 'plant/DeletePlant.html', {'plant': plant})


def search_plants(request):
    query = request.GET.get('query', '').strip()  # Get the query from the request, default to empty string
    plants = Plant.objects.all()  # Default: show all plants

    if query:  # If there is a query, filter plants
        plants = plants.filter(name__icontains=query)  # Case-insensitive search for plant name

    return render(request, 'plant/search.html', {'plants': plants, 'query': query})

