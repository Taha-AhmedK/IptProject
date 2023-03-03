
from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login_view, name='login'),
    path('logout', views.logout_view, name='logout'),
    path('signup', views.signup, name='signup'),
    path('category/<str:cat>', views.category, name='category'),
    path('categories', views.all_categories, name='all_categories'),
    path('dish/<str:name>', views.view_recipe, name='view_recipe'),
    path('add_recipe', views.add_recipe, name='add_recipe'),
    path('view_profile', views.view_profile, name='view_profile'),
    path('dish_addfav/<int:id>', views.recipe_addfav, name='recipe_addfav'),
    path('dish_remfav/<int:id>', views.recipe_remfav, name='recipe_remfav'),
    path('dish_edit/<int:id>', views.recipe_edit, name='recipe_edit'),
    path('checkout', views.checkout, name='checkout'),
    path('confirm', views.confirm_order, name='confirm_oder'),
    path('get_order_list', views.get_order_list, name='get_order_list'),
]
