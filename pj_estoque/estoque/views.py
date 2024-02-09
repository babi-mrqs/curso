from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, UpdateView,DeleteView, View
from django.urls import reverse_lazy
from django.contrib.auth import logout
from .models import Estoque


class EstoqueListView(ListView):
    model = Estoque

class EstoqueCreateView(CreateView):
    model = Estoque
    fields = ['nome', 'descricao', 'quantidade', 'preco']
    success_url = reverse_lazy("estoque_list")

class EstoqueUpdateView(UpdateView):
    model = Estoque
    fields = ['nome', 'descricao', 'quantidade', 'preco']
    success_url = reverse_lazy("estoque_list")


class EstoqueDeleteView(DeleteView):
    model = Estoque
    success_url = reverse_lazy("estoque_list")

class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('login')