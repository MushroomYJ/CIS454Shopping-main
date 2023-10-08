from django.urls import path

from . import views

urlpatterns = [
	path('', views.store, name="store"),
	path('cart/', views.cart, name="cart"),
	path('checkout/', views.checkout, name="checkout"),

	path('login/', views.log_in, name="login"),
	path('signup/', views.sign_up, name="signup"),
	path('logout/', views.log_out, name='logout'),

	path('update_item/', views.updateItem, name="update_item"),

	path('process_order/', views.processOrder, name="process_order"),

]