from __future__ import unicode_literals
from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User
# Create your models here.
class Store(models.Model):
	class Meta:
		db_table = "store"
	store_name = models.CharField(max_length = 200)
	store_address = models.CharField(max_length = 200)
	store_phone = models.IntegerField()
	store_mobile_phone = models.IntegerField()
	store_user_add_store = models.ForeignKey(User)
	store_number_of_items_in_store = models.IntegerField()

	def __str__(self):
		return self.store_name
	

class Items(models.Model):
	class Meta:
		db_table = "items"
	items_name = models.CharField(max_length = 200)
	items_manufactured = models.CharField(max_length = 200)
	items_price = models.IntegerField()
	items_user_add = models.ForeignKey(User)
	items_store_item_is_placed = models.ForeignKey(Store)

	def __str__(self):
		return self.items_name