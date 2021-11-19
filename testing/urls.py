from django.urls import path
from . import views
urlpatterns = [
    path('home/', views.index, name='home'),
    path('home/<slug:pk>/', views.profile, name='sign-up'),
    path('login/', views.Loginpage, name='Login'),
    path('logout/', views.logoutpage, name="log-out"),
    path('comment/', views.comment, name='comment'),
    path('hii/<str:pk>/', views.delete, name='delete'),
    path('create/', views.create, name='create'),
    path('register/', views.register, name='register')
    # path('main/', views.mainview, name="main")
]