from django.contrib import admin

# Register your models here.

from .models import User,Dish,Category,DishImage,Order

admin.site.register(User)

admin.site.register(Category)
admin.site.register(Order)

class RecipeImageInline(admin.TabularInline):
    model = DishImage
    extra = 3

class PropertyAdmin(admin.ModelAdmin):
    inlines = [ RecipeImageInline, ]

admin.site.register(Dish, PropertyAdmin)