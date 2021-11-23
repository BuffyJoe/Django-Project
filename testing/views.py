from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.models import User
from .models import post, topic, comments
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import postform, commentform
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from .forms import postform, commentform
# Create your views here.

def index(request):
     posts = post.objects.all().order_by('-created')
     topics = topic.objects.all()
     comment = comments.objects.all()
     context = {
          'posts' : posts, 
          'topics' : topics, 
          'comments' : comment
          }
     return render(request, 'base/home.html', context)

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
def topicview(request, pk):
     try:
          topics = topic.objects.get(topic=pk)
          posts = topics.post_set.all()
          context = {
               'topic' : topics,
               'posts' : posts, 
          }
          return render(request, 'base/topicview.html', context)
     except Exception as exc:
          return render(request, 'base/topicview.html', {'found' : False})

@login_required(login_url='Login')
def postview(request, pk):
     context = {}
     posts = post.objects.get(id=pk)
     liked_people = posts.liked.all()
     try:
          comment = posts.comments_set.all()
     except:
          pass
     form = commentform()
     context = {
               'posts' : posts,
               'comments' : comment,
               'form' : form,
               'liked_people' : liked_people,
          }
     if request.method == 'POST':
          form = commentform(request.POST)
          if form.is_valid():
               forms = form.save(commit=False)
               forms.posts = post.objects.get(id=pk)
               forms.owner = request.user
               forms.save()
               return render(request, 'base/postview.html', context)
     return render(request, 'base/postview.html', context)

@login_required(login_url='Login')
def like_post(request):
     user = request.user
     if request.method == 'POST':
          post_id = request.POST.get('post_id')
          post_obj = post.objects.get(id=post_id)
          if user in post_obj.liked.all():
               post_obj.liked.remove(user)
          else:
               post_obj.liked.add(user)
     return HttpResponseRedirect(post_id)

@login_required(login_url='Login')
def createroom(request):
     form = postform()
     if request.method == 'POST':
        form = postform(request.POST)
        if form.is_valid():
          new_form = form.save(commit=False)
          new_form.author = request.user
          new_form.save()
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

@login_required(login_url='Login')
def deletepost(request, pk):
     form = post.objects.get(id=pk)
     try:
          if request.method == 'POST':
               form.delete()
               return redirect('home')
     except:
          return render(request, 'base/delete.html', {'postt':form})
     return render(request, 'base/delete.html', {'form' : form, 'postt' : True})

@login_required(login_url='Login')
def comment(request, pk):
     form = commentform()
     context = {
          'form' : form
     }
     if request.method == 'POST':
          form = commentform(request.POST)
          if form.is_valid():
               forms = form.save(commit=False)
               forms.posts = post.objects.get(id=pk)
               forms.owner = request.user
               forms.save()
               return redirect('home')
     return render(request, 'base/comment.html', context)

@login_required(login_url='Login')
def deletecomment(request, pk):
     form = comments.objects.get(id=pk)
     try:
          if request.method == 'POST':
               form.delete()
               return redirect('home')
     except:
          return render(request, 'base/delete.html', {'post':form})
     return render(request, 'base/delete.html', {'form' : form, 'commentt' : True})

def signup(request):
     form = UserCreationForm()
     if request.method == 'POST':
          form = UserCreationForm(request.POST)
          if form.is_valid():
               user = form.save(commit=False)
               user.username = user.username.lower()
               user.save()
               login(request, user)
               return redirect('home')
     return render(request, 'base/register.html', {'form' : form, 'sign' : True})

