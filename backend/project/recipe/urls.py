from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import RecipeView, IngredientView, StepView

urlpatterns = [
    path('api/recipes', RecipeView.as_view()),
    path('api/recipes/<int:id>', RecipeView.as_view()),

    path('api/recipes/<int:recipeId>/ingredients', IngredientView.as_view()),
    path('api/recipes/<int:recipeId>/ingredients/<int:id>', IngredientView.as_view()),

    path('api/recipes/<int:recipeId>/steps', StepView.as_view()),
    path('api/recipes/<int:recipeId>/steps/<int:id>', StepView.as_view()),
]