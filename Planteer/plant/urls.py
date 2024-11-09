from django.urls import path
from . import views

app_name = 'plant'

urlpatterns = [
    path('all/', views.all_plants, name='all_plant'),
    path('search/', views.search_plants, name='search'),
    path('new/', views.add_plant, name='add_plant'),
    path('<int:plant_id>/detail/', views.plant_detail, name='plant_detail'),
    path('<int:plant_id>/update/', views.update_plant, name='update_plant'),
    path('<int:plant_id>/delete/', views.delete_plant, name='delete_plant'),
]
