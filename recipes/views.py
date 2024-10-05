from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from allauth.account.views import LoginView as AllauthLoginView, SignupView as AllauthSignupView, LogoutView as AllauthLogoutView
from .models import Recipe
from .forms import RecipeForm

# Home page view (no recipes displayed here)
def index(request):
    return render(request, 'index.html')

# Recipes list view (renders the recipes.html template)
def recipe_list(request):
    recipes = Recipe.objects.all()
    paginator = Paginator(recipes, 6)  # Show 14 recipes per page
    page_number = request.GET.get('page')  # Get the current page number from the request
    page_obj = paginator.get_page(page_number)  # Get the recipes for the current page

    return render(request, 'recipes.html', {'page_obj': page_obj})

# Recipe detail view
def recipe_detail(request, slug):
    recipe = get_object_or_404(Recipe, slug=slug)
    return render(request, 'recipes/recipe_detail.html', {'recipe': recipe})    

# Create recipe view
@login_required  # Require user to be logged in to access this view
def create_recipe(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.author = request.user
            recipe.save()
            messages.success(request, 'Recipe added successfully!')
            return redirect('recipe_list')
    else:
        form = RecipeForm()
    
    return render(request, 'recipes/create_recipe.html', {'form': form})   

# Custom login view using allauth
class LoginView(AllauthLoginView):
    template_name = 'account/login.html'

# Custom signup view using allauth
class SignupView(AllauthSignupView):
    template_name = 'account/signup.html'

# Custom logout view using allauth
class LogoutView(AllauthLogoutView):
    template_name = 'account/logout.html'