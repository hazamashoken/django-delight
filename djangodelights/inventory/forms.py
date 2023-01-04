from django import forms
from inventory.models import Ingredient, MenuItem, RecipeRequirement, Purchase

class IngredientForm(forms.ModelForm):
	class Meta:
		model = Ingredient
		fields = '__all__'

class MenuItemForm(forms.ModelForm):
	class Meta:
		model = MenuItem
		fields = '__all__'

class RecipeRequirementForm(forms.ModelForm):
	class Meta:
		model = RecipeRequirement
		fields = '__all__'

class PurchaseForm(forms.ModelForm):
	class Meta:
		model = Purchase
		fields = '__all__'

