from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('update/', views.user_update, name='user_update'),
    path('password/', views.change_password, name='change_password'),
    path('reservation/', views.reservation, name='reservation'),
    path('deletereservation/<int:id>', views.delete_reservation, name='delete_reservation'),
    path('addreservation/<int:id>', views.add_reservation, name='add_reservation'),
]
