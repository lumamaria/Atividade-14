from django.shortcuts import render, get_object_or_404
from .models import Aluno

def alunos_list(request):
    alunos = Aluno.objects.all()
    return render(
        request,'aluno/alunos_list.html',{'alunos': alunos})


def aluno_detalhe(request, id):
    aluno = get_object_or_404(Aluno, id=id)

    return render(
        request,'aluno/aluno_detail.html',{'aluno': aluno})

