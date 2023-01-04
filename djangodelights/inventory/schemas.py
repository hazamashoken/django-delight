from ninja import Schema, ModelSchema
from inventory.models import Ingredient, MenuItem, RecipeRequirement, Purchase

class IngredientOut(ModelSchema):
	class Config:
		model = Ingredient
		model_fields = ['name', 'unit', 'prices', 'quantity']

class IngredientIn(Schema):
	name: str
	unit: str
	prices: float
	quantity: float

class PurchaseOut(ModelSchema):
	class Config:
		model = Purchase
		model_fields = ['menu_item', 'timestamp']

class PurchaseIn(Schema):
	menu_item_id: int

class MenuItemOut(ModelSchema):
	class Config:
		model = MenuItem
		model_fields = ['title', 'price']

class RecipeRequirementOut(ModelSchema):
	class Config:
		model = RecipeRequirement
		model_fields = ['ingredient', 'quantity']

class RecipeRequirementIn(Schema):
	ingredient_id: int
	quantity: float

class MenuItemIn(Schema):
	title: str
	price: float
	ingredients: list[RecipeRequirementIn]
