from django.urls import path
from . import views

urlpatterns = [
    path("", view=views.GardensListView.as_view()),
    path("register/", view=views.GardenCreateView.as_view()),
    path("garden-info/", view=views.GardensInfoListView.as_view()),
    path("garden-info/<str:id>/", view=views.GardenInfosListView.as_view()),
    path("garden-info/register/", view=views.GardenInfoCreateView.as_view()),
]
