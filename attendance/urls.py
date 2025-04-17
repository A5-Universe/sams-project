from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('login/', views.login_view, name='login'),
    path('add-student/', views.add_student, name='add_student'),
    path('delete-student/', views.delete_student, name='delete_student'),
    path('edit-attendance/', views.edit_attendance, name='edit_attendance'),
    path('mark-attendance/', views.mark_attendance, name='mark_attendance'),
    path('view-attendance/', views.view_attendance, name='view_attendance'),
]
