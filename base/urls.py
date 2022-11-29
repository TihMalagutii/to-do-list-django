from django.urls import path
from .views import ListaDisciplina, DetalheDisciplina, CriarDisciplina, EditarDisciplina, ExcluirDisciplina, Login, Cadastro, CriarTarefa, EditarTarefa, ExcluirTarefa, downloadPdf
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', Login.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('cadastro/', Cadastro.as_view(), name='cadastro'),
    path('', ListaDisciplina.as_view(), name='disciplinas'),
    path('disciplina/<int:pk>/', DetalheDisciplina.as_view(), name='disciplina'),
    path('criar-disciplina', CriarDisciplina.as_view(), name='criar-disciplina'),
    path('editar-disciplina/<int:pk>/', EditarDisciplina.as_view(), name='editar-disciplina'),
    path('excluir-disciplina/<int:pk>/', ExcluirDisciplina.as_view(), name='excluir-disciplina'),
    path('criar-tarefa', CriarTarefa.as_view(), name='criar-tarefa'),
    path('editar-tarefa/<int:pk>/', EditarTarefa.as_view(), name='editar-tarefa'),
    path('excluir-tarefa/<int:pk>/', ExcluirTarefa.as_view(), name='excluir-tarefa'),
    path('downloadpdf/', downloadPdf, name='downloadpdf'),
    ]
