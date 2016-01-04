from django.conf.urls import patterns, include, url

urlpatterns = patterns ('',
		url(r'^$', 'shop.views.index'),
		url(r'^search/', 'shop.views.search'),
		url(r'^stores/all/$', 'shop.views.stores'),
		url(r'^stores/(?P<store_id>\d+)/$', 'shop.views.store'),
		# add store
		url(r'^store/add/(?P<user_id>\d+)/$', 'shop.views.addstore'),
		url(r'^store/addstore/$', 'shop.views.add_store'),
		#add product
		url(r'^products/add/(?P<user_id>\d+)/$', 'shop.views.addproduct'),
		url(r'^store/addproducts/$', 'shop.views.add_items'),
		#delete
		url(r'^delete/(?P<store_id>\d+)/$','shop.views.delete_store'),
		url(r'^delete/items/(?P<items_id>\d+)/$','shop.views.delete_items'),
		#edit store
		url(r'^update/(?P<store_id>\d+)/$','shop.views.editstore'),
		url(r'^store/editdata/$', 'shop.views.editdatastore'),
		#edit items
		url(r'^update/items/(?P<items_id>\d+)/$','shop.views.edititems'),
		url(r'^items/editdata/$', 'shop.views.editdataitems'),
		url(r'^page/(\d+)/$', 'shop.views.stores'), # - pagination
		url(r'^user/(?P<user_id>\d+)/$', 'shop.views.user_account'),
		
	)