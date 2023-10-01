from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('base/', views.BASE, name='base'),
    path('', views.INDEX, name='index'),
    path('signup/', views.signup, name='signup'),

    # Include authentication URLs
    path('accounts/', include('django.contrib.auth.urls')),

    # addcart
    path('cart/add/<int:id>/', views.cart_add, name='cart_add'),
    path('cart/item_clear/<int:id>/', views.item_clear, name='item_clear'),
    path('cart/item_increment/<int:id>/', views.item_increment, name='item_increment'),
    path('cart/item_decrement/<int:id>/', views.item_decrement, name='item_decrement'),
    path('cart/cart_clear/', views.cart_clear, name='cart_clear'),
    path('cart/cart-detail/', views.cart_detail, name='cart_detail'),


    #contact us
    path('contact_us/',views.Contact_page,name="Contact_page"),

    #checkout page
    path('checkout/',views.CheckOut,name='checkout'),

    #orderpage
    path('order/',views.Your_Order,name='Your_Order'),

   # search
    path('search/',views.Search,name='search'),
    path('account/', views.Account, name='account'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
