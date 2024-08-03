from django.shortcuts import render
from products.models import Products
from categories.models import Category
from carousel.models import Carousel
from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.sessions.models import Session
from django.contrib.auth import authenticate, login as auth_login, logout
from django.core.paginator import Paginator
from faq.models import Faq


def home(request):
    productdata = Products.objects.all()
    categorydata = Category.objects.all()
    carouseldata = Carousel.objects.all()

    data = {
        "products": productdata,
        "categories": categorydata,
        "carousels": carouseldata,
    }
    return render(request, "index.html", data)


def contact(request):
    return render(request, "contact.html")


def login(request):
    if request.user.is_authenticated:
        return redirect("home")
    else:
        return render(request, "login.html")


def log_inUser(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            username = request.POST["username"]
            password = request.POST["password"]
            if not username or not password:
                messages.error(request, "Please Fill All The Fields!")
                return redirect("login")
            user = authenticate(request, username=username, password=password)
            if user is not None:
                messages.success(request, "Login Successful!")
                auth_login(request, user)
                request.session["username"] = user.username
                return redirect("home")
            else:
                messages.error(request, "Login Failed! Cheack Your Credentials!")
                return redirect("login")
        else:
            messages.error(request, "invalid Command")
            return render(request, "login.html")
    else:
        return redirect("home")


def log_out_user(request):
    if request.user.is_authenticated:
        logout(request)
        request.session.flush()
        messages.success(request, "Successfully Logout!")
        return render(request, "login.html")
    else:
        return redirect("login")


def signup(request):
    if request.user.is_authenticated:
        return redirect("home")
    else:
        return render(request, "signup.html")


def productDetails(request , id):
    productsdetails = Products.objects.get(id__exact = id)

    data = {
        'products': productsdetails,
    }

    return render(request, "productdetail.html" , data)


def products(request):
    productdata = Products.objects.all()
    productdata = Paginator(productdata , 4)
    if 'page' in request.GET:
        page_number = request.GET["page"]
    else :
        page_number = 1
    page_obj = productdata.get_page(page_number)
    totalpage = [x+1 for x in range(productdata.num_pages)]
    data = {
        "products": page_obj,
        "totalpages": totalpage,
       
    }

    return render(request, "products.html", data)


def searchResult(request):
    searchresults = request.GET['search']
    searchterm = Products.objects.filter(title__icontains = searchresults)
    data = {
        'searchterm' : searchterm
    }
    return render(request, "search_results.html" , data)





def productResult(request, category):
    productsbycat = Products.objects.filter(category_id=category)

    data = {
        "productsbycat": productsbycat,
    }

    return render(request, "product_results.html", data)


def register_user(request):
    if not request.user.is_authenticated:
        first_name = request.POST["first_name"]
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        if not username or not first_name or not email or not password:
            messages.error(request, "Please Fill All The Fields Correctly!")
            return render(request, "signup.html")
        else:
            if User.objects.filter(username=username).exists():
                messages.error(request, "Username Already Register")
                return render(request, "signup.html")
            elif User.objects.filter(email=email).exists():
                print("email reg")
                messages.error(request, "Email Already Register!")
                return render(request, "signup.html")
            elif len(password) < 8:
                messages.error(request, "Password Must be 8 Characters Long!")
                return render(request, "signup.html")
            else:
                user = User.objects.create_user(
                    first_name=first_name,
                    username=username,
                    email=email,
                    password=password,
                )
                messages.success(request, "Account created successfully!")
        return render(request, "signup.html")
    else:
        return redirect("home")


