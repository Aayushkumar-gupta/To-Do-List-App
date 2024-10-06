from django.urls import path, include
from . import views


urlpatterns = [
    path("", views.home, name = "home"),
    path("create/", views.create, name = "create"),
    path("view/", views.view, name = "view"),
    path("<int:id>/", views.index, name = "index"),
    path("delete/<int:item_id>/", views.delete_task, name="delete_item"),  
    path("delete_list/<int:id>/", views.delete_list, name="delete_list"),
]