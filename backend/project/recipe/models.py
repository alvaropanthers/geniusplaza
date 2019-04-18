from django.db import models

class User(models.Model):
    username = models.CharField(max_length=200, unique=True) #unique
    email = models.CharField(max_length=200, unique=True) #unique
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    created_at = models.DateField(auto_now_add=True)

class Recipe(models.Model):
    name = models.CharField(max_length=200) #Not null
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Ingredient(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    text = models.CharField(max_length=500) #Not null
    created_at = models.DateField(auto_now_add=True)

class Step(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    step_text = models.CharField(max_length=300) #Not null
    created_at = models.DateField(auto_now_add=True)