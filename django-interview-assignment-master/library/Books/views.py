from multiprocessing import context
from django.shortcuts import render ,redirect
from django.contrib.auth import authenticate , login , logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import *
from .models import *
from .decorators import *
# Create your views here.
@login_required(login_url= 'login_page')

def home(request):
    is_lib = request.user.groups.filter(name='Librarian').exists()
    context = {
        'is_lib' : is_lib
    }
    return render(request , 'Books/Dashboard.html',context=context)

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
@login_required(login_url= 'login_page')

def booksPage(request):
    books = list(Book.objects.all())
    borrowed = Borrowed.objects.all()
    borrowed_books = []
    for x in borrowed:
        borrowed_books.append(x.borrowed_book)
    for book in borrowed_books:
        books.remove(book)
    is_lib = request.user.groups.filter(name='Librarian').exists()
    context = {
        'books':books,
       'is_lib' : is_lib
    }
    return render(request , 'Books/book_table.html' , context=context)

@login_required(login_url= 'login_page')

def get_book(request,pk):
    book = Book.objects.get(id = pk)
    user = request.user
    
    Borrowed.objects.create(borrowed_by=user,borrowed_book=book)

    return redirect('books_page')
@login_required(login_url= 'login_page')    

def userBooks(request):
    borrowed = Borrowed.objects.filter(borrowed_by = request.user)
    books = []
    for x in borrowed:
        books.append(x.borrowed_book)
    context ={'books':books}
    return render(request , 'Books/user_book_table.html' , context=context)

@login_required(login_url= 'login_page')
def return_book(request,pk):
    book = Book.objects.get(id = pk)
    Borrowed.objects.filter(borrowed_book = book).delete()
    
    return redirect('user_books')
@login_required(login_url= 'login_page')
@allowed_users(allowed_roles= ['Librarian'])
def userList(request):
    users = list(User.objects.all())
    users.remove(request.user)
    
    context = {'users':users}

    return render(request,'Books/user_table.html',context=context)
@login_required(login_url= 'login_page')
@allowed_users(allowed_roles= ['Librarian'])
def delete_user(request,pk):
    User.objects.get(id = pk).delete()
    return redirect('user_list')
@login_required(login_url= 'login_page')
@allowed_users(allowed_roles= ['Librarian'])
def update_user(request,pk):
    user = User.objects.get(id = pk)
    if request.method == 'POST':
        form = UpdateUserForm(request.POST ,  instance = user)
        if form.is_valid:
            form.save()
            return redirect('home_page')
         
    form = UpdateUserForm(instance = user)
    context = {
        'form' : form
    }
    return render(request,'Books/form.html', context)
@login_required(login_url= 'login_page')
@allowed_users(allowed_roles= ['Librarian'])
def update_books(request,pk):
    book = Book.objects.get(id = pk)
    if request.method == 'POST':
        form = BookForm(request.POST ,  instance = book)
        if form.is_valid:
            form.save()
            return redirect('books_page')
    
    form = BookForm(instance = book)
    context = {
        'form' : form    
    }
    return render(request,'Books/form.html',context)