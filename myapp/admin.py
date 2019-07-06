from django.contrib import admin
from .models import User,Categories,Product

admin.site.register(User)
admin.site.register(Categories)
#admin.site.register(Product)
# Register your models here.


#class InLineCategories(admin.TabularInline):this is used when we want to show both form on same page
    #model=Categories

class ProductAdmin(admin.ModelAdmin):
    #inlines=[InLineCategories] 
    #readonly_fields=("seller",) if editable=true
    list_display=('category','seller','name','slug','description','pics','price')#here we can also put pics
    list_display_links=('name','slug','pics')
    list_editable=('price',)
    list_filter=('category',)
    search_fields=('name','slug','price')
    fieldsets=(
        (None,{'fields':
        ('category','name','slug','description','pics','price')
        }),)



    # def combine_name_and_slug(self,obj):  this is used when we want to combaine both and pass this in list_display
        # return "{}-{}".format(obj.name,obj.slug)


admin.site.register(Product,ProductAdmin)