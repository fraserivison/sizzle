from django.urls import path
from .views import (LoginView, SignupView, recipe_detail, recipe_list,
                    create_recipe, edit_recipe, delete_recipe)
from allauth.account.views import LogoutView
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('recipes/', recipe_list, name='recipe_list'),
    path('recipe/<slug:slug>/', recipe_detail, name='recipe_detail'),
    path('accounts/login/', LoginView.as_view(), name='account_login'),
    path('accounts/signup/', SignupView.as_view(), name='account_signup'),
    path('accounts/logout/', LogoutView.as_view(), name='account_logout'),
    path('create/', create_recipe, name='create_recipe'),
    path('recipes/edit/<slug:slug>/', edit_recipe, name='edit_recipe'),
    path('recipes/delete/<slug:slug>/', delete_recipe, name='delete_recipe')
]
