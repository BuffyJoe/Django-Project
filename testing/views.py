from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from .models import people, post, topic, comments
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from time import sleep
from django.contrib.auth.decorators import login_required
from .forms import postform
from django.contrib.auth.forms import UserCreationForm

from testing import forms
# Create your views here.
def index(request):
     friend = people.objects.all()
     posts = post.objects.all()
     topics = topic.objects.all()
     comment = comments.objects.all()
     return render(request, 'base/home.html', {'friend':friend, 'posts' : posts, 'topics' : topics, 'comments' : comment})

def personalprofile(request):
     context = {}
     try:
          posts = post.objects.filter(author = request.user)
          context = {
          'posts' : posts
          }
          return render(request, 'base/profile.html', context)
     except:
          return render(request, 'base/profile.html')

@login_required(login_url='Login')
def profile(request, pk):
     try:
          topics = topic.objects.get(topic=pk)
          posts = post.objects.filter(Topic = topics)
          context = {
               'topic' : topics,
               'posts' : posts, 
          }
          return render(request, 'base/signup.html', context)
     except Exception as exc:
          return render(request, 'base/signup.html', {'found' : False})

def create(request):
     form = postform()
     if request.method == 'POST':
        form = postform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
     context = {'form': form, 'create' : True}
     return render(request, 'base/room_form.html', context)
     
def Loginpage(request): 
     if request.user.is_authenticated:
          return redirect('home')
     if request.method == 'POST':
          username = request.POST.get('username')
          password = request.POST.get('password')
          handle = request.POST.get('handle')

          try:
               user = User.objects.get(username=username)
          except:
               messages.error(request, 'User does not exist')

          user = authenticate(request,handle=handle, username=username, password=password) 
          if user is not None:
               login(request, user)
               return redirect('home')
     
     context = {'log' : True}
     return render(request, 'base/register.html', context)
def logoutpage(request):
     if request.method == 'POST':
          logout(request)
          return redirect('home')
     return render(request, 'base/logout.html')

def delete(request, pk):
     form = post.objects.get(id=pk)
     try:
          if request.method == 'POST':
               form.delete()
               return redirect('home')
     except:
          return render(request, 'base/register.html', {'post':form})
     return render(request, 'base/register.html', {'form' : form, 'create' : True})

def comment(request):
     if request.method == 'POST':
          comment = request.POST.get('comment')
          context = (comment,)
          return render(request, 'base/home.html', {'comment' : context})
     return render(request, 'base/comment.html')

def register(request):
     form = UserCreationForm()
     if request.method == 'POST':
          form = UserCreationForm(request.POST)
          if form.is_valid:
               create(User)
               form.save()
               return redirect('home')
     return render(request, 'base/comment.html', {'form' : form})

