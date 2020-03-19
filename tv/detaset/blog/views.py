from django.shortcuts import render
from .models import Cntnt
from package.models import Product
from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from django.views.generic import TemplateView

# Create your views here.
def blog_Cntnt(request,cntnt_slug=None,blog_cntnt_dtls=None):
	#product=Cntnt.product
	#name=Product.name
	slug=None
	cntnts = Cntnt.objects.all()
	cntnts1=Cntnt.objects.order_by('-created_at')[0:1]
	contxt={'cntnts':cntnts,
	'cntnts1':cntnts1
	}
	if cntnt_slug:
		product = get_object_or_404(Product, slug=cntnt_slug)
		# cntnts1=Cntnt.objects.filter(name=name)[0]
		#products=Product.objects.filter(slug=cntnt_slug)
		contxt={#'cntnts':cntnts,
		# 'cntnts1':cntnts1,
		'product':product
		}
		return render(request, 'product/details.html', contxt)
	elif blog_cntnt_dtls:
		cntnts1=Cntnt.objects.filter(slug=blog_cntnt_dtls)
		cntnts = Cntnt.objects.order_by('?')[0:3]
		contxt={'cntnts':cntnts,
		'cntnts1':cntnts1}
		return render(request, 'blog/blog_list.html', contxt)	
	else:
		return render(request, 'blog/blog_list.html', contxt)
"""def blog_cntnt_dtls(request,cntnt_slug):
	cntnt = get_object_or_404(Cntnt, id=id, slug=slug, available=True)
	#cart_product_form = CartAddProductForm()
	context = {
		 'cntnt': cntnt,
		#'cart_product_form': cart_product_form
	}
	return render(request, 'blog/blog_detls.html', context)""" 	
#def side_bar_views(request,sub_cntnt_slug=None):
