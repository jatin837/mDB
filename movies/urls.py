from django.urls import path, include
from . import views
app_name = 'movies'
urlpatterns = [
    path('', views.index, name = 'moviesindex'),
    path('<int:id>', views.details, name = 'movie-detail'),
]
