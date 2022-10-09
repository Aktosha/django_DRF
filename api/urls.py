from django.urls import path
from .views import (
    my_api_view,
    task_detail_view,
    task_create_view,
    task_update_view,
    task_delete_view
)

urlpatterns = [
    path('', my_api_view),
    path('tasks/', task_detail_view),
    path('tasks-detail/<int:id>/', task_detail_view),
    path('task-create/', task_create_view),
    path('task-update/<int:id>/', task_update_view),
    path('task-delete/<int:id>/', task_delete_view)
]
