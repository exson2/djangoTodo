from django.urls import path
from .views import todoList, todoDetail

urlpatterns = [ 
    path('',todoList.as_view(), name="todo_list"),
    path("<int:pk>", todoDetail.as_view(), name="todo-detail")
]