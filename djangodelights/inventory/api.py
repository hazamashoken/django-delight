from ninja import Router
from django.shortcuts import get_object_or_404
from inventory.schemas import IngredientOut, PurchaseOut, MenuItemOut
from inventory.models import Ingredient, MenuItem, RecipeRequirement, Purchase

router = Router()

@router.get('/ingredients/{int:ingredient_id}', response=IngredientOut)
def ingredients(request, ingredient_id: int):
	return get_object_or_404(Ingredient, pk=ingredient_id)

@router.get('/ingredients', response=list[IngredientOut])
def allingredients(request):
	data = []
	for ingredient in Ingredient.objects.all():
		data.append(ingredient)
	return data

@router.get('/menuitems/{int:menuitem_id}', response=MenuItemOut)
def menuitems(request, menuitem_id: int):
	return get_object_or_404(MenuItem, pk=menuitem_id)

@router.get('/menuitems', response=list[MenuItemOut])
def allmenuitems(request):
	data = []
	for menuitem in MenuItem.objects.all():
		data.append(menuitem)
	return data

@router.get('/purchases/{int:purchase_id}', response=PurchaseOut)
def purchases(request, purchase_id: int):
	return get_object_or_404(Purchase, pk=purchase_id)

@router.get('/purchases', response=list[PurchaseOut])
def allpurchases(request):
	data = []
	for purchase in Purchase.objects.all():
		data.append(purchase)
	return data

