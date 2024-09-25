from django.urls import path
from . import views

urlpatterns = [
    path('faculties/', views.faculty_list, name='faculty_list'),
    path('kafedras/', views.kafedra_list, name='kafedra_list'),
    path('groups/', views.group_list, name='group_list'),
    path('students/', views.student_list, name='student_list'),
    path('teachers/', views.teacher_list, name='teacher_list'),
    path('subjects/', views.subject_list, name='subject_list'),
    path('', views.home, name="home")
]
