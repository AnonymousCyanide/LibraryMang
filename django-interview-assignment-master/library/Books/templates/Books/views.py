from django.shortcuts import render , redirect
from .models import *
from .forms import *
from django.contrib import messages
from django.contrib.auth import authenticate , login , logout
from django.contrib.auth.decorators import login_required
from .decorators import *
#from django.contrib.auth.forms import UserCreationForm
# Create your views here.
@login_required(login_url= 'login_page')
@allowed_users(allowed_roles= ['admin'])
def home(requests):
    orders = Order.objects.all()
    customers = Customer.objects.all()
    order_count = orders.count()
    customer_count = customers.count()
    delivered = orders.filter(status = 'Delivered').count()
    pending = orders.filter(status = 'Pending').count()
    context = {
        'orders' : orders,
        'customers' : customers,
        'customer_count' : customer_count,
        "order_count" : order_count,
        'pending' : pending,
        'delivered' : delivered
    }
    
    return render(requests , 'accounts/dashboard.html',context)
@login_required(login_url= 'login_page')
def product(requests):
    products = Product.objects.all()
    context = {'products' : products}
    return render(requests , 'accounts/products.html',context )
@login_required(login_url= 'login_page')
def customer(requests, pk):
    customer = Customer.objects.get(id = pk)
    orders = customer.order_set.all()
    order_count = orders.count()
    context = {
        'customer' : customer,
        'orders' : orders,
        'order_count' : order_count
    }
    return render(requests , 'accounts/customer.html',context)
@login_required(login_url= 'login_page')
def createOrder(request):
    if request.method == 'POST':
        #print(request.POST)
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    form = OrderForm
    context = {'form':form}
    return render(request , 'accounts/form.html' , context)
@login_required(login_url= 'login_page')
def updateOrder(request,pk):
    if request.method == 'POST':
        order = Order.objects.get(id = pk)
        form = OrderForm(request.POST , instance=order)
        if form.is_valid:
            form.save()
            return redirect('/')
    order = Order.objects.get(id = pk)
    form = OrderForm(instance= order)
    context = {'form':form}
    return render(request , 'accounts/form.html' , context)
@login_required(login_url= 'login_page')
def deleteOrder(request,pk):
    item = Order.objects.get(id = pk)
    if request.method == "POST":
        item.delete()
        return redirect('/')
    
    context = {
        'item':item
    }
    return render(request , 'accounts/delete.html',context)
@login_required(login_url= 'login_page')
def createCustomer(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('/')

    form = CustomerForm
    context = {
        'form' : form
    }
    return render(request , 'accounts/form.html' , context)
@login_required(login_url= 'login_page')
def updateCustomer(request , pk):
    customer = Customer.objects.get(id = pk)
    if request.method == 'POST':
        form = CustomerForm(request.POST ,  instance = customer)
        if form.is_valid:
            form.save()
            return redirect('/')
         
    form = CustomerForm(instance = customer)
    context = {
        'form' : form
    }
    return render(request,'accounts/form.html', context)

@unauthenticated_user
def registerPage(request):
    
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid:
            print('Valid B')
            try :
                form.save()
                messages.success(request, 'Register Succesfull')
                return redirect('login_page')
            except :
                messages.error(request, 'Invalid Credentials')
                return redirect('register_page')
    form = CreateUserForm()

    context = {'form' : form,}
    return render(request,'accounts/register.html',context)
@unauthenticated_user
def loginPage(request):
    
    if request.method == 'POST':
       username = request.POST.get('username')
       pwd = request.POST.get('password')
       user = authenticate(request , username = username , password = pwd)
       if user is not None:
            login(request , user)
            return redirect('home')
       else :
            messages.info(request , 'Wrong username or password')
            return redirect('login_page')

    context = {}
    return render(request,'accounts/login.html',context)
def logoutUser(request):
    logout(request)

    return redirect('login_page')
def userView(request):

    return render(request,'accounts/user.html')