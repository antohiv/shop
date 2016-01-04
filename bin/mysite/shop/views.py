from django.shortcuts import render, render_to_response,redirect
from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context, RequestContext
from shop.models import Store, Items
from django.core.paginator import Paginator
from django.contrib import auth
from django.core.context_processors import csrf
from forms import StoreForm,ItemsForm,EditStoreForm,EditItemsForm
from django.contrib.auth.models import User
# Create your views here.

def store_list(request):
	store = Store.objects.order_by('store_name')
	template = get_template('list_magazin.html')
	context = RequestContext(request,{
		'latest_store_list': store
		})
	return HttpResponse(template.render(context))

# Search code.
def search_form(request):
    return render(request, 'search_form.html')
 
def search(request):
    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
       	store = Store.objects.filter(store_name__icontains=q)
        return render(request, 'search_results.html',
            {'store': store, 'query': q,
            'username':auth.get_user(request).username, 
            'user_id':auth.get_user(request).id})
    else:
        return render(request, 'search_form.html', {'error': True})


#link
def index(request):
    return render_to_response('index.html',{'stores': Store.objects.order_by('?')[:5], 'username':auth.get_user(request).username, 'user_id':auth.get_user(request).id})

# All magazins + pagination
def stores(request, page_number=1):
    all_store = Store.objects.all()
    current_page = Paginator(all_store, 4)
    return render_to_response('list_magazin.html', {'stores': current_page.page(page_number), 'username':auth.get_user(request).username, 'user_id':auth.get_user(request).id})

def store(request, store_id=1):
    return render_to_response('magazin.html', {'store': Store.objects.get(id=store_id), 'products': Items.objects.filter(items_store_item_is_placed = store_id), 'username':auth.get_user(request).username, 'user_id':auth.get_user(request).id})

#user_account
def user_account(request, user_id=1):
    return render_to_response('my_account.html', {'store': Store.objects.filter(store_user_add_store=user_id), 'products': Items.objects.filter(items_user_add= user_id), 'username':auth.get_user(request).username,'user_id':auth.get_user(request).id})

# page add store
def addstore(request, user_id=1):
    add_store = StoreForm()
    args = {}
    args.update(csrf(request))
    args['form'] = add_store
    args['username']= auth.get_user(request).username
    args['user_id'] = auth.get_user(request).id
    return render_to_response('addstore.html',args)

# page add items
def addproduct(request, user_id=1):
    add_items = ItemsForm()
    args = {}
    args.update(csrf(request))
    args['form'] = add_items
    args['username']= auth.get_user(request).username
    args['user_id'] = auth.get_user(request).id
    return render_to_response('addproducts.html',args)

#add store
def add_store(request,user_id=1):
    if request.POST:
        user = auth.get_user(request).id
        form = StoreForm(request.POST)
        if form.is_valid():
            Store = form.save(commit=False)
            Store.store_user_add_store = request.user
            form.save()
    return redirect('/')

def add_items(request,user_id=1):
    if request.POST:
        user = auth.get_user(request).id
        form = ItemsForm(request.POST)
        if form.is_valid():
            Items = form.save(commit=False)
            Items.items_user_add = request.user
            form.save()
    return redirect('/')

#Edit form
def editstore(request,store_id):

    queryset = Store.objects.get(id=store_id)
    if request.POST:
        form=EditStoreForm(request.POST,instance=queryset)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        edit_store = EditStoreForm(instance=queryset)
        args = {}
        args.update(csrf(request))
        args['form'] = edit_store
        args['username']= auth.get_user(request).username
        args['user_id'] = auth.get_user(request).id
        return render_to_response('edit_store.html',args)
     
def editdatastore(request):
    if form.is_valid():
        form.save()
        return redirect('/')

def delete_store(request, store_id):
   emp = Store.objects.get(id = store_id)
   emp.delete()
   return redirect('/')

# DElete/Edit items
def edititems(request,items_id):

    queryset = Items.objects.get(id=items_id)
    if request.POST:
        form=EditItemsForm(request.POST,instance=queryset)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        edit_items = EditItemsForm(instance=queryset)
        args = {}
        args.update(csrf(request))
        args['form'] = edit_items
        args['username']= auth.get_user(request).username
        args['user_id'] = auth.get_user(request).id
        return render_to_response('edit_product.html',args)
     
def editdataitems(request):
    if form.is_valid():
            form.save()
            return redirect('/')

def delete_items(request, items_id):
   emp = Items.objects.get(id = items_id)
   emp.delete()
   return redirect('/')