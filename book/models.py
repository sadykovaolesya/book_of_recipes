from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings


class Author(AbstractUser):
    email = models.EmailField(max_length=128, unique=True)

    class Meta:
        app_label = "book"
        verbose_name = "Автор"
        verbose_name_plural = "Авторы"

    def __str__(self):
        return self.username


class Ingredient(models.Model):
    title = models.CharField(
        "Название", max_length=255, db_index=True
    )

    class Meta:
        app_label = "book"
        verbose_name = "Ингредиент"
        verbose_name_plural = "Ингредиенты"

    def __str__(self):
        return self.title


class Recipe(models.Model):
    title = models.CharField(
        "Название", max_length=255, db_index=True
    )

    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, verbose_name="Автор", related_name="recipe", on_delete=models.PROTECT
    )

    img_recipe = models.ImageField(upload_to='img_recipe')

    description = models.CharField("Описание", max_length=255, blank=True)
    text_recipe = models.TextField("Текст рецепта", blank=True)
    created_at = models.DateTimeField("Время создания записи", auto_now_add=True)
    updated_at = models.DateTimeField("Время обновления записи", auto_now=True)

    class Meta:
        app_label = "book"
        verbose_name = "Рецепт"
        verbose_name_plural = "Рецепты"

    def __str__(self):
        return self.title


class RecipeIngredient(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name="recipe_ingredient")
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE, related_name="ingredient")
    quantity = models.FloatField()
    UNITY_CHOICES = (
        ('g', 'gram'),
        ('ml', 'millilitre')

    )
    unity = models.CharField(max_length=2, choices=UNITY_CHOICES, default='g')

    class Meta:
        app_label = "book"
        verbose_name = "Ингредиент рецепта"
        verbose_name_plural = "Ингредиенты рецептов"

    def __str__(self):
        return f'{self.recipe}, {self.ingredient}, {self.quantity}, {self.unity}'
    