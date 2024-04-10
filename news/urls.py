from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.create_post, name='add'),
    path('update_post/<str:title>/<str:new_title>/', views.update_post, name='update_post'),
    path('delete_post/<str:title>', views.delete_post, name='delete_post')
]