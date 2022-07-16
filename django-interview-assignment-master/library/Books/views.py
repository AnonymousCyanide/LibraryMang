from django.shortcuts import render ,redirect
from django.contrib.auth import authenticate , login , logout
from django.contrib import messages
from .forms import *
from .models import *
# Create your views here.

def home(request):
    return render(request , 'Books/Dashboard.html')

def loginPage(request):
    if request.method == 'POST':
       username = request.POST.get('username')
       pwd = request.POST.get('password')
       user = authenticate(request , username = username , password = pwd)
       if user is not None:
            login(request , user)
            return redirect('home_page')
       else :
            #messages.info(request , 'Wrong username or password')
            return redirect('login_page')
    return render(request, 'Books/login.html')
def logoutUser(request):
    logout(request)

    return redirect('login_page')
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
    return render(request,'Books/register.html',context)

def booksPage(request):
    books = list(Book.objects.all())
    borrowed = Borrowed.objects.filter(status = 'Borrowed')
    borrowed_books = []
    for x in borrowed:
        borrowed_books.append(x.borrowed_book)
    for book in borrowed_books:
        books.remove(book)

    context = {'books':books}
    return render(request , 'Books/book_table.html' , context=context)
def get_book(request):
    pass
