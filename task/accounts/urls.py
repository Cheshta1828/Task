from django.urls import path
from .views import login_view,admin_view,customer_view,logout_view,home_view
from . import views

urlpatterns = [
    path('login/', login_view, name='login_view'),
    path('admin_view',admin_view,name='admin_view'),
    path('customer_view',customer_view,name='customer_view'),
    path('logout/', logout_view, name='logout'),
    path('',home_view,name='home_view'),
    path('createorder/<int:id>', views.createorder, name='createorder'),
    
   
]