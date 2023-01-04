from django.shortcuts import render, redirect
from django.db.models import Sum, F
from django.views.generic import ListView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from typing import Any, Dict

from inventory.models import Ingredient, MenuItem, RecipeRequirement, Purchase
from inventory.forms import IngredientForm, MenuItemForm, RecipeRequirementForm, PurchaseForm
# Create your views here.

class HomeView(LoginRequiredMixin, TemplateView):
	template_name = "inventory/home.html"

	def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
		context = super().get_context_data(**kwargs)
		context["ingredients"] = Ingredient.objects.all()
		context["menu_items"] = MenuItem.objects.all()
		context["purchases"] = Purchase.objects.all()
		context["reciperequirements"] = RecipeRequirement.objects.all()
		return context

class IngredientListView(LoginRequiredMixin, ListView):
	model = Ingredient
	template_name = 'inventory/ingredient_list.html'

class IngredientCreateView(LoginRequiredMixin, CreateView):
	model = Ingredient
	form_class = IngredientForm
	template_name = 'inventory/add_ingredient.html'

class IngredientUpdateView(LoginRequiredMixin, UpdateView):
	model = Ingredient
	form_class = IngredientForm
	template_name = 'inventory/update_ingredient.html'

class IngredientDeleteView(LoginRequiredMixin, DeleteView):
	model = Ingredient
	form_class = IngredientForm
	template_name = 'inventory/delete_ingredient.html'

	def post(self, request, *args, **kwargs):
		self.object = self.get_object()
		success_url = self.get_success_url()
		self.object.delete()
		return redirect(success_url)

class MenuItemListView(LoginRequiredMixin, ListView):
	model = MenuItem
	template_name = 'inventory/menu_list.html'

class MenuItemCreateView(LoginRequiredMixin, CreateView):
	model = MenuItem
	form_class = MenuItemForm
	template_name = 'inventory/add_menu_item.html'

class MenuItemUpdateView(LoginRequiredMixin, UpdateView):
	model = MenuItem
	form_class = MenuItemForm
	template_name = 'inventory/update_menu_item.html'

class RecipeRequirementCreateView(LoginRequiredMixin, CreateView):
	model = RecipeRequirement
	form_class = RecipeRequirementForm
	template_name = 'inventory/add_recipe_requirement.html'

class RecipeRequirementUpdateView(LoginRequiredMixin, UpdateView):
	model = RecipeRequirement
	form_class = RecipeRequirementForm
	template_name = 'inventory/update_recipe_requirement.html'

class RecipeRequirementDeleteView(LoginRequiredMixin, DeleteView):
	model = RecipeRequirement
	form_class = RecipeRequirementForm
	template_name = 'inventory/delete_recipe_requirement.html'
	success_url = '/menu'

	def post(self, request, *args, **kwargs):
		self.object = self.get_object()
		success_url = self.get_success_url()
		self.object.delete()
		return redirect(success_url)

class PurchaseListView(LoginRequiredMixin, ListView):
	model = Purchase
	template_name = 'inventory/purchase_list.html'

class PurchaseCreateView(LoginRequiredMixin, CreateView):
	model = Purchase
	form_class = PurchaseForm
	template_name = 'inventory/add_purchase.html'

	def post(self, request):
		menu_item_id = request.POST['menu_item']
		menu_item = MenuItem.objects.get(id=menu_item_id)
		requirements = menu_item.reciperequirement_set
		purchase = Purchase.objects.create(menu_item=menu_item)

		for requirement in requirements.all():
			required_ingredient = requirement.ingredient
			required_ingredient.quantity -= requirement.quantity
			required_ingredient.save()

		purchase.save()
		return redirect("/purchases")

class ReportView(LoginRequiredMixin, TemplateView):
	template_name = "inventory/reports.html"

	def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
		context = super().get_context_data(**kwargs)
		context["purchases"] = Purchase.objects.all()
		revenue = Purchase.objects.aggregate(
			revenue=Sum("menu_item__price"))["revenue"]
		total_cost = 0
		for purchase in Purchase.objects.all():
			for recipe_requirement in purchase.menu_item.reciperequirement_set.all():
				total_cost += recipe_requirement.ingredient.prices * recipe_requirement.quantity

		context["revenue"] = revenue
		context["total_cost"] = total_cost
		context["profit"] = revenue - total_cost

		return context

def log_out(request):
	logout(request)
	return redirect("/")
