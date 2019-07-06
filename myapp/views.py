from django.shortcuts import render,redirect,HttpResponse
from django.views.generic import ListView ,DetailView,CreateView,View,FormView ,DeleteView ,UpdateView
from .forms import login_user,ChangepasswordForm,PasswordResetForm,Categories_list,Product_list,Sellerform,buyerform,imageForm
#from django.contrib.auth.models import User
from .models import User
from django.contrib.auth import authenticate,login,logout
from .models import Product,Categories,Product,buyeraddress,image
from django.contrib.auth.decorators import login_required 
from cart.forms import CartForm
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.forms import modelformset_factory
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string
from django.db.models import Q


def Home(request):
    obj=Categories.objects.all()
    
    '''
    for i in obj:
        for j in i.product_set.all():
            print(i)
            print(j.name)
            print(j.price)
    '''
    context={"Products":obj,"categories_list":obj} #in this first key is to show products and another for category in dropdown
    return render (request,'home.html',context)
'''   
class Home(ListView):
    model = Product
    template_name="home.html"
    
    def get_context_data(self,**kwargs):
        kwargs['categories_list'] = Categories.objects.all()
        return super().get_context_data(**kwargs)

'''
'''
def DetailProduct(request,slug):
    data = Product.objects.all()
    form_class = CartForm()
    return render(request,'Productdetail.html',{'data':data,'form_class':CartForm})
'''
class DetailProduct(DetailView):
    model = Product
    form_class = CartForm
    template_name = "Productdetail.html"

    
    def get_context_data(self,**kwargs):
        kwargs['categories_list'] = Categories.objects.all()
        return super().get_context_data(**kwargs)
    
'''
def Register(request):
    if request.method=="POST":
        form=Userform(request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            first_name=form.cleaned_data['first_name']
            last_name=form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            User.objects.create_user(username=username,first_name=first_name,last_name=last_name,email=email,password=password)
            return redirect('myapp/login')
    else:
        form=Userform()
    return render(request,'register.html',{'form':form})
'''
class SellerregisterView(CreateView):
    model = User
    form_class = Sellerform
    template_name = 'register.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'seller'
        return super().get_context_data(**kwargs)

    def get_context_data(self,**kwargs):
        kwargs['categories_list'] = Categories.objects.all()
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        return redirect('/myapp/login') 

class buyerregisterView(CreateView):
    model = User
    form_class = buyerform
    template_name = 'register.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'buyer'
        return super().get_context_data(**kwargs)

    def get_context_data(self,**kwargs):
        kwargs['categories_list'] = Categories.objects.all()
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        return redirect('/myapp/login')       

def Loginuser(request):
    if request.method=="POST":
        logindata=login_user(request.POST)
        if logindata.is_valid():
            user_id=logindata.cleaned_data['user_id']
            password=logindata.cleaned_data['password']
            User=authenticate(username=user_id,password = password)
            if User is not None:
                if User.buyer==True:
                    #print(User.buyer)
                    login(request,User)
                    return redirect('/myapp')
                else:
                    login(request,User)
                    return redirect('/myapp/selleraddproduct')
            else:
                return HttpResponse("Login Failed")        
                    
    form = login_user()
    categories_list = Categories.objects.all()
    return render(request,'login.html',{"form":form,"categories_list":categories_list})

def logoutuser(request):
	logout(request)
	return redirect('login')

def changepassworduser(request):
    user=request.user
    if request.method=="POST":
        form=ChangepasswordForm(request.POST)
        if form.is_valid():
            user=request.user
            old_password=form.cleaned_data['old_password']
            new_password=form.cleaned_data['new_password']
            confirm_password=form.cleaned_data['confirm_password']
            if (new_password==confirm_password) and request.user.check_password(f'{old_password}'):              
                request.user.set_password(new_password)              
                request.user.save()
                logout(request)
                return redirect('login')
            else:
                print('hello world')
    else:
        form=ChangepasswordForm()
    return render(request,"changepassword.html",{'form':form})
       

class AddCategories(SuccessMessageMixin,CreateView, ListView):
    model=Categories
    template_name="sellercategory.html"
    form_class=Categories_list
    success_url="/myapp/selleraddcategory"  #this is used to redirect page individualy
    success_message = "%(name)s was created successfully"
    '''
    def get_context_data(self,**kwargs):
        kwargs['categories_list'] = Categories.objects.all()
        return super().get_context_data(**kwargs)
    '''

# add product by seller name
class AddProduct(SuccessMessageMixin,CreateView):
    model=Product
    template_name="sellerproduct.html"
    form_class = Product_list
    success_url="/myapp/selleraddproduct"  #this is used to redirect page individualy
    success_message = "%(name)s was Added successfully"

    def get_context_data(self,**kwargs):
        kwargs['categories_list'] = Categories.objects.all()
        return super().get_context_data(**kwargs)
'''
    def form_valid(self,form,request):
        user=form.save(self.request)
        print(user)
        return HttpResponse("Thank You Seller")
'''


# add product by seller name
def AddProduct(request):
    if request.method=="POST":
        form=Product_list(request.POST , request.FILES)
        if form.is_valid():
            
            form.save(request)
            messages.success(request,"product added sucessfully")
            return redirect("/myapp/selleraddproduct")

    else:
        form=Product_list()
    context={"form":form}
    return render(request,"sellerproduct.html",context)


def delete(request,id):
	if request.method=="POST":
		obj=Product.objects.get(id=id)
		obj.delete()
		return redirect('/myapp/sellerproductshow/')

	obj=Product.objects.get(id=id)
	return render(request,'confirm_delete.html',{'key':obj})
'''
class DeleteProduct(DeleteView):
	model = Product
	template_name = "confirm_delete.html"
	success_url ="/myapp/sellerproductshow"
'''
class UpdateProduct(UpdateView):
    model=Product
    template_name="sellerproduct.html"
    form_class = Product_list
    success_url = "/myapp/sellerproductshow"

    def get_context_data(self,**kwargs):
        kwargs['categories_list'] = Categories.objects.all()
        return super().get_context_data(**kwargs)

'''
def edit(request,id):
	obj=Product.objects.get(id=id)
	if request.method=="POST":
		form = Product_list(request.POST,instance=obj)#instance used to rewrite same date
		if form.is_valid():
			form.save()
			return redirect('/myapp/sellerproductshow')
		else:
			return HttpResponse('Not Valid')
	return render(request,'sellerproduct.html',{'obj':obj})
'''


class BasicUploadView(View):
    def get(self, request):
        form = Product_list()
        return render(self.request, 'sellerproduct.html', {'form': form})

    def post(self, request):
        form = Product_list(self.request.POST, self.request.FILES)
        if form.is_valid():
            form.save()
            #data = {'is_valid': True, 'name': Product.pics.name, 'url': Product.pics.url}
            return redirect("/myapp/selleraddproduct")
        else:
            #data = {'is_valid': False}
            return redirect("/myapp/selleraddproduct")


def search(request):
    categories_list = Categories.objects.all() 
    if request.method=="POST":
        match=request.POST["search"]
        if match:
            data=Product.objects.filter(name__icontains=match)
            if data:
                return render(request,'productlist.html',{'product_list':data,"categories_list":categories_list})
            else:
                messages.error(request,'no result found')
        else:
            messages.error(request,'Enter something to search')
            return redirect('/myapp')
    

'''
class buyeraddress(CreateView, ListView):    
    model=buyeraddress
    template_name="buyeraddress.html"
    form_class=buyeraddressform

    
    #success_url="/myapp/selleraddcategory"  #this is used to redirect page individualy
    #success_message = "%(name)s was created successfully"
'''
# Create your views here.

def display(request,slug):
    categories_list = Categories.objects.all()#to show category in dropdown
    s = Categories.objects.get(slug = slug)
    data= Product.objects.filter(category = s.id) #if we want to set limit then we use[1:10] 
    return render(request,'productlist.html',{'product_list':data,"categories_list":categories_list})



def sellerproductshow(request):
    user=request.user
    products=Product.objects.all()
    Electronic=products.filter(Q(seller=user) & Q(category__name__icontains="Electronics"))
    electronics1=Electronic.first().category.name
    #print(electronics1)
    #print(Electronic)
    Fashion=products.filter(Q(seller=user) & Q(category__name__icontains="fashion"))
    Sports=products.filter(Q(seller=user) & Q(category__name__icontains="sports"))
    context={"Electronic":Electronic,"Fashion":Fashion,"Sports":Sports,}
    return render(request,'sellerproductshow.html',context)
