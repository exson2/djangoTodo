from rest_framework import generics
from .models import ToDoItem
from .serializers import ToDoItemSerializer

class todoList(generics.ListCreateAPIView):
    queryset = ToDoItem.objects.all()
    serializer_class = ToDoItemSerializer

class todoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ToDoItem.objects.all()
    serializer_class = ToDoItemSerializer
