from django.shortcuts import render
from rest_framework.decorators import api_view
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from todoapp.models import TodoModel
from todoapp.serializers import TodoModelSerializer,TodoDescriptioniSerializer
from django.shortcuts import redirect
from rest_framework.views import APIView
from django.urls import reverse
# Create your views here.


class GetTasks(APIView):
    def get(self, request):
        user = request.user
        todoList = TodoModel.objects.filter(user = user).order_by('priority')
        response = TodoModelSerializer(todoList,many= True)
        return Response(response.data)




class UpdateDescription(APIView):

    def post(self, request, id=None):

        task = TodoModel.objects.filter(user=request.user,id = id).first()
        if task:
            requestData = TodoDescriptioniSerializer(instance=task,data = request.data)

            if requestData.is_valid():
                requestData.save()
                return redirect(reverse('AllTasks'))
        else:
            return Response("Task Not Found",status=status.HTTP_404_NOT_FOUND)
    
        return Response(requestData.errors,status=status.HTTP_400_BAD_REQUEST)

class CreateTask(APIView):

    def post(self, request):
        user = request.user
        requestData = TodoDescriptioniSerializer(data=request.data)
        if requestData.is_valid():
            taskWithLeastPriority = TodoModel.objects.filter(user= user).order_by('-priority').first()
            if taskWithLeastPriority:
                currentPriority = taskWithLeastPriority.priority
            else:
                currentPriority = 0
                
            todoTask = TodoModel(description=request.data.get('description',''),priority=currentPriority+1,isDone = False,user = user)
            todoTask.save()
            return redirect(reverse('AllTasks'))

        return Response(requestData.errors,status=status.HTTP_400_BAD_REQUEST)


class DeleteTask(APIView):

    def get(self, request, id):
        
        taskToDelete = TodoModel.objects.filter(id=id,user=request.user)
        if taskToDelete:
            taskToDelete.delete()
            return redirect(reverse('AllTasks'))

    
        return Response("Record Not Found",status=status.HTTP_404_NOT_FOUND)

class UpdateTaskStatus(APIView):

    def get(self, request, id):
        
        taskToDelete = TodoModel.objects.filter(id=id,user=request.user).first()
        if taskToDelete:
            taskToDelete.isDone = True
            taskToDelete.save()
            return redirect(reverse('AllTasks'))

    
        return Response("Record Not Found",status=status.HTTP_404_NOT_FOUND)

class SwitchPriority(APIView):

    def post(self, request):
       
        task1 = TodoModel.objects.filter(user=request.user,id=request.data.get('task1_id','0')).first()
        task2 = TodoModel.objects.filter(user=request.user,id=request.data.get('task2_id','0')).first()
        if task1 and task2:
            task1Priority = task1.priority
            task1.priority = task2.priority
            task2.priority = task1Priority

            task1.save()
            task2.save()
            return redirect(reverse('AllTasks'))

    
        return Response("Record Not Found",status=status.HTTP_404_NOT_FOUND)