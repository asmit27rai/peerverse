from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list,name='post_list'),
    path('generate/', views.post_generate,name='post_generate'),
    path('<int:post_id>/delete/', views.post_delete,name='post_delete'),
    path('<int:post_id>/edit/', views.post_edit,name='post_edit'),
    path('register/', views.register,name='register'),
    path('compose/', views.compose_message, name='compose_message'),
    path('inbox/', views.inbox, name='inbox'),
    path('delete_message/<int:message_id>/', views.delete_message, name='delete_message'),
    path('profile/', views.profile_dashboard, name='profile_dashboard'),
    path('user/<str:username>/', views.user_dashboard, name='user_dashboard'),
    path('download/<int:post_id>/', views.download_file, name='download_file'),
]