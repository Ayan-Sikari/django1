from django.urls import path
from .views import index,TodoListCreateView, TodoDetailView

urlpatterns = [
    path('', index, name='index'),
    path('todos/', TodoListCreateView.as_view(), name='todo-list-create'),
    path('todos/<int:pk>/', TodoDetailView.as_view(), name='todo-detail'),
]
