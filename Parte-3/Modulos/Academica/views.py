from django.shortcuts import render, redirect, get_object_or_404
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate , logout
from .models import Task
from .forms import TaskForm, UpdateTaskForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm

# DIRECCIONES a las que se referencian los hrefs

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('index')  # Redirige a la lista de tareas después de registrarse
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')  # Redirige a la lista de tareas después de iniciar sesión
    else:
        form = AuthenticationForm()
    return render(request, 'index.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('index')  

def formularioContacto(request):
    return render (request ,"formularioContacto.html")
def contactar (request):
    if request.method=="POST":
        asunto = request.POST["txtAsunto"]
        mensaje= request.POST["txtMensaje"]+"/ Email" + request.POST["txtEmail"]
        email_desde= settings.EMAIL_HOST_USER
        email_para = ["isaac.martel.b@uni.pe"]
        send_mail(asunto,mensaje,email_desde,email_para,fail_silently=False)
        return render(request , "contactoExitoso.html")
    return render(request , "formularioContacto.html")


def index(request):
    if request.user.is_authenticated:
        return task_list(request)
    else:
        return login_view(request)
    

@login_required
def task_list(request):
    tasks = Task.objects.filter(student=request.user)
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.student = request.user
            task.save()
            return redirect('index')
    else:
        form = TaskForm()
    return render(request, 'index.html', {'tasks': tasks, 'form': form})

@login_required
def update_task(request, task_id):
    task = get_object_or_404(Task, id=task_id, student=request.user)
    if request.method == 'POST':
        form = UpdateTaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = UpdateTaskForm(instance=task)
    # return render(request, 'update_task.html', {'form': form, 'task': task})

@login_required
def edit_task(request, task_id):
    task = get_object_or_404(Task, id=task_id, student=request.user)
    if request.method == 'POST':
        new_description = request.POST.get('new_description')
        if new_description:
            task.description = new_description
            task.save()
        return redirect('index')
    else:       
        return redirect('index')


@login_required
def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id, student=request.user)
    if request.method == 'POST':
        task.delete()
        return redirect('index')
    # return render(request, 'delete_task.html', {'task': task})