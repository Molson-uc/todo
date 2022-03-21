from django.urls import path
from . import views


urlpatterns = [
    path("", views.list_tasks, name="list-tasks"),
    path("update/<int:_id>/", views.update_task, name="update-task"),
    path("delete/<int:_id>/", views.delete_task, name="delete-task"),
]
