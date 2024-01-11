from django.shortcuts import render,redirect
from testapp.forms import product,product_bills
from testapp.models import Bills,product_details


# Create your views here.
def home(request):
    register = False
    form=product
    kalyan= product_details.objects.all()
    if request.method == 'POST':
        form = product(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            print("sucessfull")
            register = True
        
    return render(request,"home.html",{"form":form,'register':register,'kalyan':kalyan})

def bills(request):
    submit = False
    pavan = product_bills
    if request.method == 'POST':
        pavan = product_bills(request.POST)
        if pavan.is_valid():
            pavan.save()
            print("successfull")
            Quantity = pavan.cleaned_data['Quantity']
            price = pavan.cleaned_data['price']
            total_amount = Quantity*price
            submit = True
        return render(request,'bills.html',{'Quantity':Quantity,'price':price,'total_amount':total_amount,'submit':submit})
    return render(request,'bills.html',{"pavan":pavan})

def total_bills(request):
    kumar=Bills.objects.all()
    return render(request,"total_bills.html",{'kumar':kumar})

