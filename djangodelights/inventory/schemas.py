from ninja import Schema, ModelSchema
from inventory.models import Ingredient, MenuItem, RecipeRequirement, Purchase

class IngredientOut(ModelSchema):
	class Config:
		model = Ingredient
		model_fields = ['name', 'unit', 'prices', 'quantity']

class PurchaseOut(ModelSchema):
	class Config:
		model = Purchase
		model_fields = ['menu_item', 'timestamp']

class MenuItemOut(ModelSchema):
	class Config:
		model = MenuItem
		model_fields = ['title', 'price']
