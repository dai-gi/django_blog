from django.urls import path
from blog import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='post_detail'), 
    path('post/new/', views.CreatePostView.as_view(), name='post_new'), 
    path('post/<int:pk/edit/', views.CreatePostView.as_view(), name='post_edit'), 
]