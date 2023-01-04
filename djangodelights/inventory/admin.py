from django.contrib import admin
from inventory.models import Ingredient, MenuItem, RecipeRequirement, Purchase
# Register your models here.

[admin.site.register(X) for X in [RecipeRequirement, MenuItem, Ingredient, Purchase]]

