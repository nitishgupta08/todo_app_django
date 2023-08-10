"""
API views for Todo
"""
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from todo.models import Todo

from .serializers import TodoSerializer


# Create your views here.


class TodoListCreate(ListCreateAPIView):
    """
    Todo List/Create View
    """

    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


class TodoDetail(RetrieveUpdateDestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
