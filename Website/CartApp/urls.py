from django.urls import path
from . import views
app_name='CartApp'

urlpatterns=[
    path('add/<int:product_id>/',views.Cart_add,name='cart_add'),
    path('',views.Cart_detail,name='cart_detail'),
    #path('remove/<int:product_id>/',views.Cart_remove,name='cart_remove'),
    #path('remove_all/<int:product_id>/',views.Cart_remove_all,name='cart_remove_all'),
]
