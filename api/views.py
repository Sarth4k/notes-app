from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from task.models import Task
from .serializers import TaskSerializer


@api_view(['GET','POST'])
def notes_list(request):
    if request.method=='GET':
        notes = Task.objects.all()
        serializer = TaskSerializer(notes,many = True)
        return Response(serializer.data)
    if request.method == 'POST':
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.error,status=status.HTTP_404_BAD_REQUEST)
