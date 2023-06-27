from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .forms import LoginForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.contrib.auth import logout
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .forms import LoginForm
from .models import auth,customer
from django.contrib.auth.models import User

from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Sum
from django.urls import reverse
from django.shortcuts import redirect


@login_required
def admin_view(request):
    return render(request, 'admin_view.html')
@login_required
def customer_view(request):
    return render(request, 'customer_view.html')
@login_required
def logout_view(request):
    logout(request)
    return redirect('home_view') 

def home_view(request):
    return render(request, 'home_view.html')


def login_view(request):
    if request.method == 'POST':
        print("loginview")
        form = LoginForm(request.POST)
        print("form")
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            print(user)
            print(user.id)
            if user is not None:
                try:
                    print("not none")
                    user_auth = auth.objects.get(user=user)
                    
                    if  user_auth.is_admin:
                        login(request, user)
                        ins=customer.objects.all()
                        customer1_user = User.objects.get(username="customer1")

                        customer1 = customer.objects.filter(orderedby=customer1_user)
                        customer2_user = User.objects.get(username="customer2")

                        customer2 = customer.objects.filter(orderedby=customer2_user)
                        customer1_quantity = customer1.aggregate(Sum('quantity'))['quantity__sum']
                        customer1_weight = customer1.aggregate(Sum('weight'))['weight__sum']
                        customer1_boxcount = customer1.aggregate(Sum('box_count'))['box_count__sum']
                        customer2_quantity = customer2.aggregate(Sum('quantity'))['quantity__sum']
                        customer2_weight = customer2.aggregate(Sum('weight'))['weight__sum']
                        customer2_boxcount = customer2.aggregate(Sum('box_count'))['box_count__sum']
        
        
                        total_quantity = customer1_quantity + customer2_quantity
                        total_weight = customer1_weight + customer2_weight
                        total_boxcount = customer1_boxcount + customer2_boxcount
                        print("Customer 1 Quantity:", customer1_quantity)
                        print("Customer 1 Weight:", customer1_weight)
                        print("Customer 1 Boxcount:", customer1_boxcount)
                        print("Customer 2 Quantity:", customer2_quantity)
                        print("Customer 2 Weight:", customer2_weight)
                        print("Customer 2 Boxcount:", customer2_boxcount)
                        print("Total Quantity:", total_quantity)
                        print("Total Weight:", total_weight)
                        print("Total Boxcount:", total_boxcount)
                        context = {
                            
                           
                            "customer1_quantity": customer1_quantity,
                            "customer2_quantity": customer2_quantity,
                            "total_quantity": total_quantity,
                            "customer1_weight": customer1_weight,
                            "customer2_weight": customer2_weight,
                            "total_weight": total_weight,
                            "customer1_boxcount": customer1_boxcount,
                            "customer2_boxcount": customer2_boxcount,
                            "total_boxcount": total_boxcount
                                                                     }

                        

                        return render(request, 'admin_view.html',context)
                    elif  not user_auth.is_admin:
                        login(request, user)
                        print("redirecting to create order")
                        context ={"id":user.id}
                      
                        
                        return render(request, 'customer_view.html',context)
                    else:
                        form.add_error(None, 'Invalid ID or password.')
                except auth.DoesNotExist:
                    form.add_error(None, 'Invalid ID or password.')
            else:
                form.add_error(None, 'Invalid ID or password.')
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})
@login_required
def createorder(request,id):
    print("create order called")
    print(id)
    if request.method == 'POST':
        order_date = request.POST.get('order_date')
        company = request.POST.get('company')
        owner = request.POST.get('owner')
        item = request.POST.get('item')
        quantity = request.POST.get('quantity')
        weight = request.POST.get('weight')
        request_for_shipment = request.POST.get('request_for_shipment')
        tracking_id = request.POST.get('tracking_id')
        shipment_size = request.POST.get('shipment_size')
        box_count = request.POST.get('box_count')
        specification = request.POST.get('specification')
        checklist_quantity = request.POST.get('checklist_quantity')
        
        userinstance=User.objects.get(id=id)
        print(userinstance)
        

        # Create a new instance of the Customer model
        cus = customer(
            order_date=order_date,
            company=company,
            owner=owner,
            item=item,
            quantity=quantity,
            weight=weight,
            request_for_shipment=request_for_shipment,
            tracking_id=tracking_id,
            shipment_size=shipment_size,
            box_count=box_count,
            specification=specification,
            checklist_quantity=checklist_quantity,
            orderedby=userinstance
        )

        
        cus.save()

    return HttpResponse('Data saved successfully!')