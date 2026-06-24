from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from rest_framework import status
from task.models import Task
from .serializers import TaskSerializer
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token
from rest_framework_simplejwt.tokens import RefreshToken
@api_view(['GET','POST'])
def notes_list(request):
    if request.method=='GET':
        notes = Task.objects.filter(task_manager=request.user)
        serializer = TaskSerializer(notes,many = True)
        return Response(serializer.data)
    if request.method == 'POST':
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(task_manager=request.user)
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
  
@api_view(['PUT'])
def notes_update(request,pk):
    notes = Task.objects.get(id=pk)
    serializer = TaskSerializer(notes,data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def notes_detail(request,pk):
    notes = Task.objects.get(id=pk)
    serializer = TaskSerializer(notes)
    return Response(serializer.data)

@api_view(['DELETE'])
def notes_delete(request,pk):
    notes = Task.objects.get(id=pk)
    notes.delete()
    return Response({"message": "Task deleted"}, status=status.HTTP_200_OK)


#login api
@api_view(['POST'])
@permission_classes([AllowAny])
def login_view(request):
    username = request.data.get('username')
    password = request.data.get('password')
    user = authenticate(
        username=username,
        password=password
    )
    if user is not None:
        refresh = RefreshToken.for_user(user)
        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token)
        })
    return Response(
        {
            'error':'Wrong username or password'
        },
        status=status.HTTP_400_BAD_REQUEST
    )
    
#REGISTER API
@api_view(['POST'])
@permission_classes([AllowAny])
def register_view(request):
    username = request.data.get('username')
    password = request.data.get('password')
    if not username or not password:
        return Response(
            {
                "error":"Username and password required"
            },
            status=400
        )
    if User.objects.filter(
        username=username
    ).exists():
        return Response(
            {
                "error":"Username already taken"
            },
            status=400
        )
    User.objects.create_user(
        username=username,
        password=password
    )
    return Response(
        {
            "message":"User created successfully"
        },
        status=201
    )