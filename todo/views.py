from rest_framework import generics
from .models import Todo
from .serializers import TodoSerializer
from django.shortcuts import render

def index(request):
    return render(request, 'todo/index.html')

# View for listing and creating tasks
class TodoListCreateView(generics.ListCreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

# View for retrieving, updating, and deleting a task
class TodoDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
