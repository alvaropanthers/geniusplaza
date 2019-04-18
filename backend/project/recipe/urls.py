from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import RecipeView

urlpatterns = [

    #URL should be change to api/recipe
    path('api/recipes', RecipeView.as_view()), #Returns all recipies


    path('api/recipes/<int:id>', RecipeView.as_view()), #Returns a recipe given the userId
    

    #path('api/recipes', RecipeView.as_view()), #Accepts post request to create new recipies


    path('api/recipes/<int:id>', RecipeView.as_view()), #Updates a recipe


    #path('api/recipe/<int:recipeId', RecipeView.as_view()), #Deletes a recipe

]