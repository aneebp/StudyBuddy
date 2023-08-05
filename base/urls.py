from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name="home"),
    path('login/',views.LoginPage,name='login'),
    path('register/',views.RegisterPage,name='register'),
    path('logout/',views.LogoutPage,name='logout'),
    path('room/<str:pk>',views.room,name="room"),
    path('create_room/',views.createRoom,name="create-room"),
    path('update_room/<str:pk>',views.updateRoom,name="update-room"),
    path('delete_room/<str:pk>',views.deleteRoom,name="delete-room"),


]