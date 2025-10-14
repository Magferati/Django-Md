from django.contrib import admin
from django.urls import path
from.views import flower1 , get_all , delete,update,get_data_by_id
urlpatterns = [
   # path("home/",home, name=home),
    path("flower1/", flower1, name="flower1"),
    path('get-all/', get_all, name='get-all'),
    path("delete/<int:id>/", delete, name="delete"),
    path("items/<int:id>/", get_data_by_id, name="get_data_by_id"),
    path("update/<int:id>/<str:title>/<str:describtion>/",update,name="update"),
]