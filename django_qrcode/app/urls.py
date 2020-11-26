from django.urls import path
from .views import HomeView, QrList
urlpatterns = [
    path('', HomeView, name="home"),
    path('list/', QrList, name="list"),
]
