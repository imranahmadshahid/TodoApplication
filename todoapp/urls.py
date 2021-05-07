from django.conf.urls import url
from django.urls import path, include
from todoapp import views
from rest_framework.authtoken import views as authviews


urlpatterns = [
    path('api/todolist', views.GetTasks.as_view(),name='AllTasks'),
    path('api/updatelist/<int:id>', views.UpdateDescription.as_view(),name='updatedescription'),
    path('api/createtask', views.CreateTask.as_view(),name='createtask'),
    path('api/deletetask/<int:id>', views.DeleteTask.as_view(),name='deletetask'),
    path('api/UpdateTaskStatus/<int:id>', views.UpdateTaskStatus.as_view(),name='updatataskstatus'),
    path('api/updatepriority', views.SwitchPriority.as_view(),name='updatepriority'),
    path('api-token-auth', authviews.obtain_auth_token)
] 