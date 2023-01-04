from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
	path('', views.HomeView.as_view(), name='home'),
	path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
	path('logout/', auth_views.LogoutView.as_view(), name='logout'),
	path('ingredients/', views.IngredientListView.as_view(), name='ingredients'),
	path('ingredients/new/', views.IngredientCreateView.as_view(), name='add_ingredient'),
	path('ingredients/<slug:pk>/update/', views.IngredientUpdateView.as_view(), name='update_ingredient'),
	path('ingredients/<slug:pk>/delete/', views.IngredientDeleteView.as_view(), name='delete_ingredient'),
	path('menu/', views.MenuItemListView.as_view(), name='menu'),
	path('menu/new/', views.MenuItemCreateView.as_view(), name='add_menu_item'),
	path('menu/<slug:pk>/update/', views.MenuItemUpdateView.as_view(), name='update_menu_item'),
	path('reciperequirement/new', views.RecipeRequirementCreateView.as_view(), name="add_recipe_requirement"),
	path('reciperequirement/<slug:pk>/update/', views.RecipeRequirementUpdateView.as_view(), name='update_recipe_requirement'),
	path('reciperequirement/<slug:pk>/delete/', views.RecipeRequirementDeleteView.as_view(), name='delete_recipe_requirement'),
	path('purchases/', views.PurchaseListView.as_view(), name='purchases'),
	path('purchases/new/', views.PurchaseCreateView.as_view(), name='add_purchase'),
	path('report/', views.ReportView.as_view(), name='reports'),
]

