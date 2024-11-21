from django.urls import path
from . import views
urlpatterns = [
    path('categorieslist/', views.categories_list),
]
