from django.urls import path
from . import views
#app_name='Shop'

urlpatterns=[
    path('',views.Allproduct,name='allproduct'),
    path('<slug:c_slug>/',views.Allproduct,name='products_by_cat'),
    path('<slug:c_slug>/<slug:p_slug>/',views.Productdetail,name='productdetail'),
]
