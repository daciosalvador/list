from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('completa', views.completa, name='completa'),
    path('add_task', views.add_task, name='add_task'),
    path('delete_task/<str:task_id>', views.delete_task, name='delete_task'),
    path('restante', views.restante, name='restante'),
    path('task_detalhe/<str:task_id>', views.task_detalhe, name='task_detalhe'),
    path('concluir/<str:task_id>', views.concluir, name='concluir'),
    path('remover_task/<str:task_id>', views.remover_task, name='remover_task'),
    path('produtividade', views.produtividade, name='produtividade'),
]