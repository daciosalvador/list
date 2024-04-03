from django.shortcuts import render, redirect
from .models import Task

def home(request):
    tasks = Task.objects.all()
    return render(request, 'index.html', {
        'tasks': tasks,
    })


def completa(request):
    task_concluida = Task.objects.filter(completa=True)
    return render(request, 'completa.html', {
        'tasks': task_concluida,
    })

def add_task(request):
    if request.method == "POST":
        titulo = request.POST.get('titulo')
        descricao = request.POST.get('descricao')
        data = request.POST.get('data')
        time = request.POST.get('time')
        completa = False

        if titulo and data and time:
            task = Task(
                titulo=titulo,
                descricao=descricao,
                data=data,
                time=time,
                completa=completa
            )
            task.save()
            return redirect('home')
    return render(request, 'add_task.html')

def delete_task(request, task_id):
    task = Task.objects.get(id=task_id)
    return render(request, 'delete.html', {
        "task": task,
    })

def restante(request):
    task_restante = Task.objects.filter(completa=False)
    return render(request, 'restante.html', {
        'tasks': task_restante,
    })

def task_detalhe(request, task_id):
    tasks = Task.objects.get(id=task_id)
    return render(request, 'task_detalhe.html', {
        'tasks': tasks,
    })

def concluir(request, task_id):
    task = Task.objects.get(id=task_id)
    if task:
        task.completa = not task.completa
        task.save()
        return redirect('home')
    
def remover_task(request, task_id):
    task = Task.objects.get(id=task_id)
    if task:
        task.delete()
        return redirect('home')

def produtividade(request):
    tasks_total = Task.objects.count()
    task_concluidas = Task.objects.filter(completa=True).count()
    task_pendentes = Task.objects.filter(completa=False).count()
    return render(request, 'produtividade.html', {
        'tasks_total': tasks_total,
        'task_concluidas': task_concluidas,
        'task_pendentes': task_pendentes,
    })