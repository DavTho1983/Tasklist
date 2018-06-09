from django.urls import path, include
from . import views

urlpatterns = [
    path('create', views.create, name='create'),
    path('<int:task_id>', views.taskdetail, name='taskdetail'),
    path('hide/', views.hide, name='hide'),
    path('edit/<int:task_id>', views.edit, name='edit'),
    path('markcompleted/<int:task_id>', views.markcompleted, name='markcompleted'),
    path('delete/<int:task_id>', views.delete, name='delete'),
]
