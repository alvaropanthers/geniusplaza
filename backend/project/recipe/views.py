from django.shortcuts import render
from django.http import QueryDict

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import User, Recipe, Ingredient, Step
from .serializers import RecipeSerializer, IngredientSerializer, StepSerializer

class IngredientView(APIView):
    def post(self, request, recipeId):
        text = request.POST.get('text', None)

        if text:
            try:
                recipe = Recipe.objects.get(pk=recipeId)

                nIngredient = Ingredient(text=text, recipe=recipe)
                nIngredient.save()

                serializer = IngredientSerializer(nIngredient)
                data = serializer.data
                re_status = status.HTTP_201_CREATED

            except User.DoesNotExist:
                data = {'error': 'user does not exist'}
                re_status=status.HTTP_404_NOT_FOUND
        else:
            data = {'error': 'incorrect text'}
            re_status = status.HTTP_400_BAD_REQUEST

        return Response(data, status=re_status)

    def put(self, request, recipeId):
        text = request.data['text'] if 'text' in request.data else None

        if text:
            try:
                ingredient = Ingredient.objects.get(pk=recipeId)

                ingredient.text = text
                ingredient.save()

                serializer = IngredientSerializer(ingredient)
                data = serializer.data
                re_status = status.HTTP_200_OK
            except Ingredient.DoesNotExist:
                data = {'error': 'Resource does not exist'}
                re_status = status.HTTP_404_NOT_FOUND
        else:
            data = {'error': 'incorrect text'}
            re_status = status.HTTP_400_BAD_REQUEST

        return Response(data, re_status)

    #If id is represent than it returns the ingredient with the specified id
    #If id is not present than it returns all of the ingredientsq
    def get(self, request, recipeId, id=None):
        if id:
            try:
                recipe = Recipe.objects.get(pk=recipeId)
                ingredient = Ingredient.objects.get(pk=id, recipe=recipe)
                serializer = IngredientSerializer(ingredient)
                data = serializer.data
                re_status = status.HTTP_200_OK
            except (Recipe.DoesNotExist, Ingredient.DoesNotExist):
                data = {'error': 'Resource does not exist'}
                re_status = status.HTTP_404_NOT_FOUND
        else:
            ingredients = Ingredient.objects.filter(recipe_id=recipeId)
            serializer = IngredientSerializer(ingredients, many=True)
            data = serializer.data
            re_status = status.HTTP_200_OK
        
        return Response(data, status=re_status)

    def delete(self, request, recipeId, id):
        try:
            recipe = Recipe.objects.get(pk=recipeId)
            ingredient = Ingredient.objects.get(pk=id, recipe=recipe)
            ingredient.delete()
            data = ''
            re_status = status.HTTP_200_OK
        except (Recipe.DoesNotExist, Ingredient.DoesNotExist):
            data = {'error': 'Resource does not exist'}
            re_status = status.HTTP_404_NOT_FOUND  

        return Response(data, re_status)

class RecipeView(APIView):
    def post(self, request):
        recipeName = request.POST.get('name', None)
        username = request.POST.get('username', None)

        if recipeName and username:
            try:
                user = User.objects.get(username=username)

                nRecipe = Recipe(name=recipeName, user=user)
                nRecipe.save()

                serializer = RecipeSerializer(nRecipe)
                data = serializer.data
                re_status = status.HTTP_201_CREATED
            except User.DoesNotExist:
                data = {'error': 'user does not exist'}
                re_status=status.HTTP_404_NOT_FOUND
        else:
            data = {'error': 'incorrect name or username'}
            re_status = status.HTTP_400_BAD_REQUEST

        return Response(data, status=re_status)

    def put(self, request, id):
        recipeName = request.data['name'] if 'name' in request.data else None

        if recipeName:
            try:
                recipe = Recipe.objects.get(pk=id)
                recipe.name = recipeName
                recipe.save()

                serializer = RecipeSerializer(recipe)
                data = serializer.data
                re_status = status.HTTP_200_OK
            except Recipe.DoesNotExist:
                data = {'error': 'Resource does not exist'}
                re_status = status.HTTP_404_NOT_FOUND
        else:
            data = {'error': 'incorrect recipeName'}
            re_status = status.HTTP_400_BAD_REQUEST

        return Response(data, re_status)

    def get(self, request, id=None):
        if id:
            try:
                user = User.objects.get(pk=id)
                recipes = Recipe.objects.filter(user=user)
                serializer = RecipeSerializer(recipes, many=True)
                data = serializer.data
                re_status = status.HTTP_200_OK
            except (User.DoesNotExist, Recipe.DoesNotExist):
                data = {'error': 'Resource does not exist'}
                re_status = status.HTTP_404_NOT_FOUND
        else:
            recipes = Recipe.objects.all()
            serializer = RecipeSerializer(recipes, many=True)
            data = serializer.data
            re_status = status.HTTP_200_OK
        
        return Response(data, status=re_status)

    def delete(self, request, id):
        try:
            recipe = Recipe.objects.get(pk=id)
            recipe.delete()
            data = ''
            re_status = status.HTTP_200_OK
        except Recipe.DoesNotExist:
            data = {'error': 'Recipe does not exist'}
            re_status = status.HTTP_404_NOT_FOUND            
    

        return Response(data, re_status)