from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.urls import reverse_lazy
from .models import Disciplina, Tarefa
from django import forms

from django.http import FileResponse
import io
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter

import json

def downloadPdf(request):
    buf = io.BytesIO()
    c = canvas.Canvas(buf, pagesize=letter, bottomup=0)
    textobj = c.beginText()
    textobj.setTextOrigin(inch, inch)
    textobj.setFont("Helvetica", 14)
    
    disciplinas = Disciplina.objects.all()
    
    lines = []
    
    for disciplina in disciplinas:
        lines.append(disciplina.title)
        
    for line in lines:
        textobj.textLine(line)
        
    c.drawText(textobj)
    c.showPage()
    c.save()
    buf.seek(0)
    
    return FileResponse(buf, as_attachment=True, filename='disciplinas.pdf')

class TarefaForm(forms.ModelForm):
    class Meta:
       model = Tarefa
       fields = ['disciplina', 'title', 'complete']

    def __init__(self, *args, **kwargs):
       user = kwargs.pop('user')
       super(TarefaForm, self).__init__(*args, **kwargs)
       self.fields['disciplina'].queryset = Disciplina.objects.filter(user=user)

class Login(LoginView):
    template_name = 'base/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('disciplinas')

class Cadastro(FormView):
    template_name = 'base/cadastro.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('disciplinas')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(Cadastro, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('disciplinas')
        return super(Cadastro, self).get(*args, **kwargs)

class ListaDisciplina(LoginRequiredMixin, ListView):
    model = Disciplina
    context_object_name = 'disciplinas'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['disciplinas'] = context['disciplinas'].filter(user=self.request.user)
        context['count'] = context['disciplinas'].filter(complete=False).count()

        input_pesquisar = self.request.GET.get('area-pesquisar') or ''
        if input_pesquisar:
            context['disciplinas'] = context['disciplinas'].filter(title__icontains=input_pesquisar)

        context['input_pesquisar'] = input_pesquisar

        return context

class DetalheDisciplina(LoginRequiredMixin, DetailView):
    model = Disciplina
    context_object_name = 'disciplina'
    template_name = 'base/disciplina.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tarefas'] = Tarefa.objects.filter(disciplina=self.kwargs.get('pk'))
        context['countTarefas'] = context['tarefas'].filter(complete=False).count()
        return context

class CriarDisciplina(LoginRequiredMixin, CreateView):
    model = Disciplina
    fields = ['title']
    success_url = reverse_lazy('disciplinas')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(CriarDisciplina, self).form_valid(form)

class EditarDisciplina(LoginRequiredMixin, UpdateView):
    model = Disciplina
    fields = ['title', 'complete']
    success_url = reverse_lazy('disciplinas')

class ExcluirDisciplina(LoginRequiredMixin, DeleteView):
    model = Disciplina
    context_object_name = 'disciplina'
    success_url = reverse_lazy('disciplinas')

class CriarTarefa(LoginRequiredMixin, CreateView):
    model = Tarefa
    form_class = TarefaForm
    success_url = reverse_lazy('disciplinas')
    
    def get_form_kwargs(self):
        kwargs = super(CriarTarefa, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

class EditarTarefa(LoginRequiredMixin, UpdateView):
    model = Tarefa
    fields = ['disciplina', 'title', 'complete']
    success_url = reverse_lazy('disciplinas')

class ExcluirTarefa(LoginRequiredMixin, DeleteView):
    model = Tarefa
    context_object_name = 'tarefa'
    success_url = reverse_lazy('disciplinas')
