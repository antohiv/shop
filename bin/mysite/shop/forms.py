from django.forms import ModelForm
from models import Store, Items

class StoreForm(ModelForm):
	class Meta:
		model = Store
		fields = ['store_name','store_address','store_phone','store_mobile_phone','store_number_of_items_in_store']

class ItemsForm(ModelForm):
	class Meta:
		model = Items
		fields = ['items_name','items_manufactured','items_price','items_store_item_is_placed']

class EditStoreForm(ModelForm):
	class Meta:
		model = Store
		fields = ['store_name','store_address','store_phone','store_mobile_phone','store_number_of_items_in_store']

class EditItemsForm(ModelForm):
	class Meta:
		model = Items
		fields = ['items_name','items_manufactured','items_price','items_store_item_is_placed']
