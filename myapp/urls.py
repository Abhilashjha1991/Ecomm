from django.urls import path
from django.conf.urls import url,include
from django.contrib.auth import views as auth_views #predefined in django to reset pswd
from .views import Home,Loginuser,logoutuser,DetailProduct,AddCategories,AddProduct,search,sellerproductshow,UpdateProduct,changepassworduser,buyerregisterView,SellerregisterView,display,delete
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.db.models import Q


urlpatterns = [
    #path('',Home.as_view(),name="home"),
    path('',Home,name="home"),
    #path('Register/',Register,name="Register"),
    path('sellerregister/', SellerregisterView.as_view(), name='sellerregister'),
    path('buyerregister/', buyerregisterView.as_view(), name='buyerrregister'),
    path('login/',Loginuser,name="login"),
    path('logout/',logoutuser,name="logout"),
    path('changepassword/',changepassworduser,name="changepassword"),
    #path('Passwordreset/',PasswordResetView.as_view,name="Passwordreset"),
    path("detail/<str:slug>",DetailProduct.as_view(),name="detail"),
    #path("detail/<str:slug>",DetailProduct,name="detail"),
    path('selleraddcategory/',AddCategories.as_view(),name="selleraddcategory"),
    #path('selleraddproduct/',AddProduct.as_view(),name="selleraddproduct"),
    path('selleraddproduct/',AddProduct,name="selleraddproduct"),
    #path('selleraddproduct/',BasicUploadView.as_view(),name="selleraddproduct"),
    path('sellerproductshow/',sellerproductshow,name="sellerproductshow"),
    path('delete/<int:id>',delete,name="delete"),
    #path("delete/<int:pk>",DeleteProduct.as_view(),name="delete"),
    path('update/<int:pk>',UpdateProduct.as_view(),name="Update"),
    path('search/',search,name="search"),
    #path('buyeraddress/<int:id>',buyeraddress.as_view(),name="buyeraddress"),
    #path('buyeraddress/',buyeraddress.as_view(),name="buyeraddress"),
    path('display/<slug>',display,name="display"),

    #reset password urls
    #path('password_reset/', auth_views.password_reset, name='password_reset'),
    #path('password_reset/done/', auth_views.password_reset_done, name='password_reset_done'),
    #path('password_reset/confirm/(?P<uidb64>[\w-]+)/(?P<token>[\w-]+)/',auth_views.password_reset_confirm, name='password_reset_confirm'),
    #path('password_reset/complete/',auth_views.password_reset_complete, name='password_reset_complete'),
    #url('^', include('django.contrib.auth.urls')),

    path('password-reset/',auth_views.PasswordResetView.as_view(),name='password_reset'),
    path('password-reset/done/',auth_views.PasswordResetDoneView.as_view(),name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
    path('password-reset-complete/',auth_views.PasswordResetCompleteView.as_view(),name='password_reset_complete'),
    
]