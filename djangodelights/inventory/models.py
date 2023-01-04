from django.db import models

# Create your models here.
class Ingredient(models.Model):
	name = models.CharField(max_length=100)
	quantity = models.IntegerField(default=0)
	unit = models.CharField(max_length=100)
	prices = models.FloatField(default=0)

	def get_absolute_url(self):
		return "/ingredients"

	def __str__(self) -> str:
		return f"{self.name} ({self.quantity} {self.unit}) @ ${self.prices}"

class MenuItem(models.Model):
	title = models.CharField(max_length=100)
	price = models.FloatField(default=0)

	def get_absolute_url(self):
		return "/menu"

	def available(self):
		return all(X.enough() for X in self.reciperequirement_set.all())

	def __str__(self) -> str:
		return f"{self.title} @ ${self.price}"

class RecipeRequirement(models.Model):
	ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
	menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
	quantity = models.FloatField(default=0)

	def get_absolute_url(self):
		return "/menu"

	def enough(self):
		return self.quantity <= self.ingredient.quantity

	def __str__(self) -> str:
		return f"{self.ingredient} x {self.quantity} for {self.menu_item}"""

class Purchase(models.Model):
	menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
	timestamp = models.DateField(auto_now_add=True)

	def get_absolute_url(self):
		return "/purchases"

	def __str__(self) -> str:
		return f"{self.menu_item} purchased on {self.timestamp}"
