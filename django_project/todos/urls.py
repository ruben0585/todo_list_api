from django.urls import path
from .views import TaskList, TaskDetail

urlpatterns = [
    path("", TaskList.as_view(), name="taskList"),
    path("<int:pk>/", TaskDetail.as_view(), name="task_detail")
]

#el primer path es para que el usuario pueda ver la lista de tareas y el segundo path 
#es para que el usuario pueda ver la tarea especifica