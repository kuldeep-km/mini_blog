from django.shortcuts import render,HttpResponseRedirect
from .forms import SignupForm, LoginForm, BlogForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import BlogModel
from django.contrib.auth.models import Group


# Create your views here.

#Home
def home(request):
    blog = BlogModel.objects.all()
    return render(request, 'home.html',{'blog':blog})


#About
def about(request):
    return render(request,'about.html')


#Dashboard
def dashboard(request):
    blog=BlogModel.objects.all()
    if request.user.is_authenticated:
        return render(request,'dashboard.html',{'blog':blog})
    else:
        return HttpResponseRedirect('/login/')

#User logout
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')

#Signup
def user_signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user= form.save()
            group= Group.objects.get(name='Author')
            user.group.add(group)
    else:
        form = SignupForm()
    return render(request,'signup.html',{'form':form})

#Login
def user_login(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = LoginForm(request=request, data=request.POST)
            if form.is_valid():
                uname = form.cleaned_data['username']
                upass = form.cleaned_data['password']
                user = authenticate(username=uname, password=upass)
                if user is not None:
                    login(request,user)
                    messages.success(request, 'Logged in successfully')
                    return HttpResponseRedirect('/dashboard/')
        else:
            form = LoginForm()
        return render(request,'login.html',{'form':form})
    else:
        return HttpResponseRedirect('/dashboard/')
    
# Add_Blog

def add_blog(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = BlogForm(request.POST)
            if form.is_valid():
                title = form.cleaned_data['title']
                content = form.cleaned_data['content']
                blg = BlogModel(title=title, content=content)
                blg.save()
                form = BlogForm()
                #or form.save()
        else:
            form = BlogForm()
        return render(request, 'addblog.html',{'form':form})
    else:
        return HttpResponseRedirect('/login/')
    
# Update_Blog

def update_blog(request, id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            blg = BlogModel.objects.get(pk=id)
            form = BlogForm(request.POST, instance=blg)
            if form.is_valid():
                form.save()
        else:
            blg = BlogModel.objects.get(pk=id)
            form = BlogForm(instance=blg)
        return render(request, 'updateblog.html',{'form':form})
    else:
        return HttpResponseRedirect('/login/')
    
# Delete_Blog

def delete_blog(request, id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            blg = BlogModel.objects.get(pk=id)
            blg.delete()
        return HttpResponseRedirect('/dashboard/')
    else:
        return HttpResponseRedirect('/login/')