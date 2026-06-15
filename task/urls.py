from django.urls import path,include
from . import views
from . views import TaskListView,TaskDetailView,TaskCreateView,TaskUpdateView,TaskDeleteView
from users import views as user_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',TaskListView.as_view(),name='task-home'),
    path('task/<int:pk>/',TaskDetailView.as_view(),name='task-detail'),
    path('task/<int:pk>/delete/',TaskDeleteView.as_view(),name='task-delete'),
    path('task/new/',TaskCreateView.as_view(),name='task-create'),
    path('task/<int:pk>/update/',TaskUpdateView.as_view(),name='task-update'),
    path('register/',user_views.register,name='task-reg'),
    path('login/',user_views.login,name='task-login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('ckeditor/', include('ckeditor_uploader.urls')),
]
