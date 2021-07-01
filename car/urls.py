from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('addreservation/<int:id>', views.addreservation, name='addreservation'),

]
