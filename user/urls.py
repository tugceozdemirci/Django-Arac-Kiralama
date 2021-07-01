from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('update/', views.user_update, name='user_update'),
    path('password/', views.change_password, name='change_password'),
    path('reservation/', views.reservation, name='reservation'),
    path('udeletereservation/<int:id>', views.udelete_reservation, name='udelete_reservation'),
    path('uaddreservation/<int:id>', views.uadd_reservation, name='uadd_reservation'),
]
