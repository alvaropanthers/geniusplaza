from django.shortcuts import render
from django.http import QueryDict

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import User, Recipe, Ingredient, Step
from .serializers import RecipeSerializer

class RecipeView(APIView):
    #Creates one recipe (Change to POST or PUT(remember that put is idempotent))
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
        username = request.data['username'] if 'username' in request.data else None

        if recipeName and username:
            try:
                user = User.objects.get(username=username)
                recipe = Recipe.objects.get(pk=id)

                #Perhaps bad
                recipe.name = recipeName
                recipe.save()

                serializer = RecipeSerializer(recipe)
                data = serializer.data
                re_status = status.HTTP_200_OK
            except (User.DoesNotExist, Recipe.DoesNotExist):
                data = {'error': 'Resource does not exist'}
                re_status = status.HTTP_404_NOT_FOUND
        else:
            data = {'error': 'incorrect recipeName or username', 'recipeName': recipeName, 'username': username}
            re_status = status.HTTP_400_BAD_REQUEST

        return Response(data, re_status)

    #Gets recipe by a single recipe given the id or returns all recipes
    def get(self, request, id=None):
        if id:
            if isinstance(id, int):
                try:
                    #There's a better way of doing this
                    user = User.objects.get(pk=id)
                    recipes = Recipe.objects.filter(user=user)
                    serializer = RecipeSerializer(recipes, many=True)
                    data = serializer.data
                    re_status = status.HTTP_200_OK
                except (User.DoesNotExist, Recipe.DoesNotExist):
                    data = {'error': 'Resource does not exist'}
                    re_status = status.HTTP_404_NOT_FOUND
            else:
                data = {'error': 'id must be an integer'}
                re_status = status.HTTP_400_BAD_REQUEST
        else:
            recipes = Recipe.objects.all()
            serializer = RecipeSerializer(recipes, many=True)
            data = serializer.data
            re_status = status.HTTP_200_OK
        
        return Response(data, status=re_status)

    #Deletes a particular recipe
    def delete(self, request, id):
        if isinstance(id, int):
            try:
                recipe = Recipe.objects.get(pk=id)
                recipe.delete()
                data = ''
                re_status = status.HTTP_200_OK
            except Recipe.DoesNotExist:
                data = {'error': 'Recipe does not exist'}
                re_status = status.HTTP_404_NOT_FOUND            
        else:
            data = {'error': 'id must be an integer'}
            re_status = status.HTTP_400_BAD_REQUEST

        return Response(data, re_status)