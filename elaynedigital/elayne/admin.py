from django.contrib import admin
from. models import *

# Register your models here.
class Card_display(admin.ModelAdmin):
    list_display=['image','name','about']

class Testimonials_display(admin.ModelAdmin):
    list_display=['paragraph','name']

class Contact_display(admin.ModelAdmin):
    list_display=['name','email','phone','subject','message']

admin.site.register(Card,Card_display)
admin.site.register(Testimonials,Testimonials_display)
admin.site.register(Contact_us,Contact_display)