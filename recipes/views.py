from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Recipe

class RecipeListView(ListView):
    model = Recipe
    template_name = 'recipes/recipe_list.html'

class RecipeDetailView(DetailView):
    model = Recipe
    template_name = 'recipes/recipe_detail.html'

class RecipeCreateView(CreateView):
    model = Recipe
    template_name = 'recipes/recipe_form.html'
    fields = ['title', 'ingredients', 'instructions', 'cooking_time', 'image']

class RecipeUpdateView(UpdateView):
    model = Recipe
    template_name = 'recipes/recipe_form.html'
    fields = ['title', 'ingredients', 'instructions', 'cooking_time', 'image']

class RecipeDeleteView(DeleteView):
    model = Recipe
    template_name = 'recipes/recipe_confirm_delete.html'
    success_url = reverse_lazy('recipe_list')
