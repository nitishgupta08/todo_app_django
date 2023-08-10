"""
URLs for the app
"""

from django.urls import path

from .views import (
    CreateToDoView,
    DeleteToDoView,
    ListTodoView,
    TodoDetailView,
    UpdateToDoView,
)

urlpatterns = [
    path("todos/", ListTodoView.as_view(), name="home"),
    path("todo/<int:pk>/", TodoDetailView.as_view(), name="detail"),
    path("todo/create/", CreateToDoView.as_view(), name="create_todo"),
    path("todo/update/<int:pk>/", UpdateToDoView.as_view(), name="update_todo"),
    path("todo/delete/<int:pk>/", DeleteToDoView.as_view(), name="delete_todo"),
]
