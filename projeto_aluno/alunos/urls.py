from django.urls import path

from . import views

app_name = 'alunos'

urlpatterns = [
    path('', views.alunos_list, name='alunos_list'),
    path('<int:id>/', views.aluno_detalhe, name='aluno_detalhe'),
]
