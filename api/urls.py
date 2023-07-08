from django.urls import path

from .views import TodoDetail, TodoListCreate

urlpatterns = [
    path('todo/', TodoListCreate.as_view(), name="todo_list_create"),
    path('todo/<int:pk>/', TodoDetail.as_view(), name="todo_detail")
]
