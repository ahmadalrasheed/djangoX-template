from django.views.generic import TemplateView
from django.db import models
from django.shortcuts import render
from .models import Snack
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)

# Create your views here.
class SnackListView(ListView):
    template_name='pages/home.html'
    model = Snack

class SnackDetailView(DetailView):
    template_name='snack_detail_view.html'
    model = Snack
    context_object_name= 'snack_details'

class SnackCreateView(CreateView):
    template_name='snack_create_view.html'
    model = Snack
    fields = ['title' , 'purchaser', 'description']

class SnackUpdateView(UpdateView):
    template_name='snack_update_view.html'
    model = Snack
    fields = ['title' , 'purchaser', 'description']


class AboutPageView(TemplateView):
    template_name = 'pages/about.html'





