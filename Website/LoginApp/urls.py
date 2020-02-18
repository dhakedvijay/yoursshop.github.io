from django.urls import path
from . import views

app_name='LoginApp'

urlpatterns=[
    path('',views.Detail,name='detail'),
    path('login/',views.Login,name='login'),
    path('signup/',views.SignUp,name='signup'),
]
