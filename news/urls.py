from django.urls import path

# from . import views
from .views import index, create_student, list_students, get_student, update_student, delete_student, upload_image

urlpatterns = [
    path('', index, name='index'),
    # path('add/', views.create_post, name='add'),
    # path('update_post/<str:title>/<str:new_title>/', views.update_post, name='update_post'),
    # path('delete_post/<str:title>', views.delete_post, name='delete_post'),
    # path('getAllStudent', views.getStudent, name='getStudent')
    path('students/', create_student, name='create_student'),
    path('students/list/', list_students, name='list_students'),
    path('students/<int:student_id>/', get_student, name='get_student'),
    path('students/<int:student_id>/update/', update_student, name='update_student'),
    path('students/<int:student_id>/delete/', delete_student, name='delete_student'),
    path('upload/', upload_image, name='upload_image'),
]