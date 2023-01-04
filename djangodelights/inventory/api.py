from ninja import Router
from django.shortcuts import get_object_or_404
from inventory.schemas import IngredientOut, PurchaseOut, MenuItemOut, IngredientIn, PurchaseIn, MenuItemIn, RecipeRequirementOut, RecipeRequirementIn
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

@router.put('/ingredients/{int:ingredient_id}')
def update_ingredient(request, ingredient_id: int, payload: IngredientIn):
	ingredient = get_object_or_404(Ingredient, pk=ingredient_id)
	for key, value in payload.dict().items():
		setattr(ingredient, key, value)
	ingredient.save()
	return {"success": "Ingredient updated successfully.", "ingredient": ingredient}

@router.post('/ingredients')
def create_ingredient(request, payload: IngredientIn):
	ingredient = Ingredient.objects.create(**payload.dict())
	return {"success": "Ingredient created successfully.", "id": ingredient.id}

@router.delete('/ingredients/{int:ingredient_id}')
def delete_ingredient(request, ingredient_id: int):
	ingredient = get_object_or_404(Ingredient, pk=ingredient_id)
	ingredient.delete()
	return {"success": "Ingredient deleted successfully."}

@router.post('/menuitems')
def create_menuitem(request, payload: MenuItemIn):
	menuitem = MenuItem.objects.create(title=payload.title, price=payload.price)
	for ingredient in payload.ingredients:
		RecipeRequirement.objects.create(menu_item=menuitem, **ingredient.dict())
	return {"success": "Menu item created successfully.", "id": menuitem.id}

@router.put('/menuitems/{int:menuitem_id}')
def update_menuitem(request, menuitem_id: int, payload: MenuItemIn):
	menuitem = get_object_or_404(MenuItem, pk=menuitem_id)
	for key, value in payload.dict().items():
		if key != "ingredients":
			setattr(menuitem, key, value)
	menuitem.save()
	for ingredient in payload.ingredients:
		RecipeRequirement.objects.create(menu_item=menuitem, **ingredient.dict())
	return {"success": "Menu item updated successfully.", "menuitem": menuitem}

@router.delete('/menuitems/{int:menuitem_id}')
def delete_menuitem(request, menuitem_id: int):
	menuitem = get_object_or_404(MenuItem, pk=menuitem_id)
	menuitem.delete()
	return {"success": "Menu item deleted successfully."}

@router.post('/purchases')
def create_purchase(request, payload: PurchaseIn):
	purchase = Purchase.objects.create(**payload.dict())
	return {"success": "Purchase created successfully.", "id": purchase.id}

@router.put('/purchases/{int:purchase_id}')
def update_purchase(request, purchase_id: int, payload: PurchaseIn):
	purchase = get_object_or_404(Purchase, pk=purchase_id)
	for key, value in payload.dict().items():
		setattr(purchase, key, value)
	purchase.save()
	return {"success": "Purchase updated successfully.", "purchase": purchase}

@router.delete('/purchases/{int:purchase_id}')
def delete_purchase(request, purchase_id: int):
	purchase = get_object_or_404(Purchase, pk=purchase_id)
	purchase.delete()
	return {"success": "Purchase deleted successfully."}

@router.get('/reciperequirements/{int:reciperequirement_id}', response=RecipeRequirementOut)
def reciperequirements(request, reciperequirement_id: int):
	return get_object_or_404(RecipeRequirement, pk=reciperequirement_id)

@router.get('/reciperequirements', response=list[RecipeRequirementOut])
def allreciperequirements(request):
	data = []
	for reciperequirement in RecipeRequirement.objects.all():
		data.append(reciperequirement)
	return data
