from django.urls import path
from . import views
urlpatterns = [
    path('home/', views.index, name='home'),
    path('home/<str:pk>/', views.topicview, name='topic'),
    path('post/<int:pk>/', views.postview, name='post'),
    path('login/', views.Loginpage, name='Login'),
    path('logout/', views.logoutpage, name="log-out"),
    path('comment/<int:pk>/', views.comment, name='comment'),
    path('delete/<str:pk>/', views.deletepost, name='delete'),
    path('create/', views.createroom, name='create'),
    path('register/', views.signup, name='register'),
    path('profile/', views.personalprofile, name="profile"),
    path('delete-com/<str:pk>/', views.deletecomment, name='delete-comment'),
    path('post/', views.like_post, name='like_post'),
]