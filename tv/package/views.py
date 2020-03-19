from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from django.views.generic import TemplateView
from .models import Category, Product,Theme,Price_list,fest_offer

#def page(requset):
	#return HttpResponse("helloword").

def product_list(request,category_slug=None,them_slug=None,price_slug=None,offer_slug=None,cat_slug=None):
	category = None
	them_p=None
	price_r=None
	Festoffer=None
	pricer=Price_list.objects.all()
	theme=Theme.objects.all()
	festoffer = fest_offer.objects.all()
	categories = Category.objects.all()
	products = Product.objects.filter(available=True)
	offer=fest_offer.objects.order_by('-created_at')[0:1]
	context = {
		'category': category,
		'categories': categories,
		'products': products,
		'offer':offer,
		'festoffer':festoffer,
		'theme':theme,
		'pricer':pricer
	}
	if category_slug:
		category = get_object_or_404(Category, slug=category_slug )
		products = Product.objects.filter(category=category)
		context = {
		'category': category,
		'categories': categories,
		'products': products
		 } 
		return render(request, 'product/mainlist.html', context)
	
	elif them_slug:
		theme = get_object_or_404(Theme, slug=them_slug )
		products=Product.objects.filter(them_p=theme)
		context = {
		'category': category,
		'categories': categories,
		'products': products
		 }
		return render(request, 'product/mainlist.html', context) 
	elif price_slug:
		price_r= get_object_or_404(Price_list, slug=price_slug )
		products=Product.objects.filter(price_r=price_r)
		context = {
		'category': category,
		'categories': categories,
		'products': products
		 }
		return render(request, 'product/mainlist.html', context)
	elif offer_slug:
		Festoffer= get_object_or_404(fest_offer, slug=offer_slug )
		products=Product.objects.filter(name=Festoffer)
		context = {
		'category': category,
		'categories': categories,
		'products': products
		 }
		return render(request, 'product/mainlist.html', context) 	 		   
	else : 
		return render(request, 'product/slids.html', context) 
	if cat_slug:
		products = Product.objects.filter(Destinations=cat_slug)
		context = {
		'category': category,
		'categories': categories,
		'products': products
		 }
		return render(request, 'product/mainlist.html', context)
	if dest_slug:
		category=Category.Destinations.filter()
			


def product_detail(request, id, slug):
	product = get_object_or_404(Product, id=id, slug=slug, available=True)
	#cart_product_form = CartAddProductForm()
	context = {
		 'product': product,
		#'cart_product_form': cart_product_form
	}
	return render(request, 'product/details.html', context)
	