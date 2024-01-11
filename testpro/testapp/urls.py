from django.urls import path
from testapp import views

urlpatterns = [
    path("",views.home,name='home'),
    path("bills/",views.bills,name='bills'),
    path("total/",views.total_bills,name='total')
    
]