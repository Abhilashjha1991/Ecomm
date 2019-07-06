from django import forms
from .models import Categories,Product,buyeraddress,image
from .models import User
'''
class Userform(forms.ModelForm):
	username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter UserName'}),required=True,max_length=30)
	email = forms.CharField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter email'}),required=True, max_length=30)
	first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter first name'}),required=True, max_length=30)
	last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter lastname'}),required=True, max_length=30)
	password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter password'}),required=True, max_length=30)
	confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter confirm password'}),required=True, max_length=30)
	class Meta:
		model=User
		fields=['username','email','first_name','last_name','password','confirm_password']
'''
class login_user(forms.Form):
    user_id = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Username'}),required=True,max_length=30)
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter password'}),required=True, max_length=30)

class ChangepasswordForm(forms.ModelForm):
    old_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}),label="Old Password",required=True)
    new_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}),label="New Password",required=True)
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}),label="Confirm Password",required=True)

    class Meta:
        model=User
        fields=['old_password','new_password','confirm_password']


class PasswordResetForm(forms.Form):
    email = forms.CharField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter email'}),required=True, max_length=50)



class Categories_list(forms.ModelForm):
    class Meta:
        model=Categories
        fields="__all__"

class Product_list(forms.ModelForm):
    #pics = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}),required=True,)
    class Meta:
        model=Product
        fields=['category','name','description','pics','price']

    def save(self,request=None):   #this is used when we use function view
        user = super().save(commit=False)
        if request is not None:    #incase of update
            user.seller=request.user
        user.save()
        return user 

      

class imageForm(forms.ModelForm):
    pics = forms.ImageField(label='Image')    
    class Meta:
        model = image
        fields = ('pics', )



class Sellerform(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter UserName'}),required=True,max_length=30)
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter first name'}),required=True, max_length=30)
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter lastname'}),required=True, max_length=30)
    email = forms.CharField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter email'}),required=True, max_length=30)
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter password'}),required=True, max_length=30)
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter confirm password'}),required=True, max_length=30)
    class Meta:
        model=User
        fields=['username','email','first_name','last_name','password','confirm_password']

    def save(self):
        user=super().save(commit=False)
        user.seller=True
        user.set_password(self.cleaned_data["password"])
        user.save()
        return User

class buyerform(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter UserName'}),required=True,max_length=30)
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter first name'}),required=True, max_length=30)
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter lastname'}),required=True, max_length=30)
    email = forms.CharField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter email'}),required=True, max_length=30)
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter password'}),required=True, max_length=30)
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter confirm password'}),required=True, max_length=30)
    class Meta:
        model=User
        fields=['username','email','first_name','last_name','password','confirm_password']

    def save(self):
        user=super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        user.buyer=True
        user.save()
        return User