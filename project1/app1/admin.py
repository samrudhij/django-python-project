from django.contrib import admin
from .models import *
# Register your models here.
class HelpAdmin(admin.ModelAdmin):
 list_display=['myName','myEmail','msg']

class LoginAdmin(admin.ModelAdmin):
 list_display=['email','password']

class FeedbackAdmin(admin.ModelAdmin):
 list_display=['email','feedback']
class OrderAdmin(admin.ModelAdmin):
 list_display=['orderid','productId','customer','isCancelled']
class ProductAdmin(admin.ModelAdmin):
 list_display=['productId','productName','price','image']


admin.site.register(Help,HelpAdmin)
admin.site.register(Login,LoginAdmin)
admin.site.register(Feedback,FeedbackAdmin)
admin.site.register(Order,OrderAdmin)
admin.site.register(Product,ProductAdmin)

