from django.contrib import admin
from django.urls import path
<<<<<<< HEAD
from.views import create,flower1 , get_all , delete,update,get_data_by_id
urlpatterns = [
   # path("home/",home, name=home),
    path("add-items/",create, name="add-items"),
    path("flower1/", flower1, name="flower1"),
=======
from.views import flower1 , get_all , delete,update,get_data_by_id,create
urlpatterns = [
   # path("home/",home, name=home),
    path("add-item/", create , name="add-item"),
    path("flower1/", flower1, name="get-all"),
>>>>>>> e04c224e6da6ff2fe8b263b1c503f2d42e878f03
    path('get-all/', get_all, name='get-all'),
    path("delete/<int:id>/", delete, name="delete"),
    path("items/<int:id>/", get_data_by_id, name="get_data_by_id"),
    path("update/<int:id>/",update,name="update"),
]