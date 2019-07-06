from django.shortcuts import *
from django.views.decorators.http import require_POST
from myapp.models import Product
from .cart import Cart
from .forms import *
from django.http import *
from django.urls import reverse


# Create your views here.
@require_POST
def cart_add(request,product_id):
    cart= Cart(request)
    product = get_object_or_404(Product,id=product_id)
    form = CartForm(request.POST)
    # print("Form",form)
    if form.is_valid():
        # print("Hello")
        cd=form.cleaned_data
        if cd['quantity']:
            cart.add(product=product,quantity=cd['quantity'],
                    update_quantity=True)
        else:
            cart.add(product=product,quantity=1,
                    update_quantity=False)
        
    return redirect('cart_detail')    

def cart_remove(request,product_id):
    cart = Cart(request)
    product = get_object_or_404(Product,id=product_id)
    cart.remove(product)
    return redirect('cart_detail')

def cart_detail(request):
    cart = Cart(request)
    #product = get_object_or_404(Product,id=d)

    for item in cart:
        
        item['update_quantity_form'] = CartForm(initial={'quantity': item['quantity'],
                                                                   'update': True})
    
    return render(request,'cart/detail.html',{'cart':cart})
    '''
    for item in cart:
        if item['product']==product:
            cart_product=item
    form = CartForm(initial={'quantity':cart_product['quantity'],
                             'update':True})
    return render(request,'cart/detail.html',{'cart_product':cart_product,
                                         'form':form,
                                         'product':product})
    '''
    





'''# this view is for another method to create cart
def cart_create(request"):
    cart_obj=Cart.objects.create(User=None)
    print("New cart created")
    return cart_obj


def Cart_home(request):
    cart_id=request.session.get('cart_id',None)
    #if cart_id is None:
        #cart_obj=cart_createt()
        #request.session['card_id']=cart_obj.id
    #else:
    qs=Cart.objects.filter(id=cart_id) 
    if qs.count() == 1:
        print('cart Id exists')
        cart_obj=qs.first()
        if request.user.is_authenticated() and cart_obj.user is None:
            cart_obj.user=request.user
            cart_obj.save()
    else:
        cart_obj=cart_create()
        request.session['card_id']=cart_obj.id
    return render(request,'home.html',{})
'''