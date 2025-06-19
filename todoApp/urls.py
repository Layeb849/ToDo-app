
from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('', views.todo_list, name='todo_list'),
    path('addNew/', views.create_todo, name='create_todo'),
    path('update/<int:pk>', views.update_todo, name='update_todo'),
    path('complete/<int:pk>', views.statusUpdate, name='statusUpdate'),

    path('delete/<int:pk>/', views.soft_delete, name='delete_todo'),
    path('trash/', views.trash_list, name='trash_list'),
    path('restore/<int:pk>/', views.restore_todo, name='restore_todo'),
    path('delete-permanent/<int:pk>/', views.delete_permanently, name='delete_permanent'),
   
]
