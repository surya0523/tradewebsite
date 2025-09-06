from django.shortcuts import render, redirect
from .models import BlogPost, Category
from .forms import PartnerForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from .forms import LoginForm
from .forms import RegisterForm
from django.contrib.auth.models import User



def index(request):
    categories = Category.objects.all()
    active_category = request.GET.get("category")
 
    if active_category:
        posts = BlogPost.objects.filter(category__name=active_category).order_by("-date")[:6]
    else:
        posts = BlogPost.objects.all().order_by("-date")[:6]
 
    return render(request, "traco/index.html", {
        "categories": categories,
        "active_category": active_category,
        "posts": posts,
    })

def home(request):
        return render(request, "traco/home.html",)

def about_view(request):
    return render(request, "traco/about.html")


def partner_view(request):
 
    form = PartnerForm()
    return render(request, 'traco/partner.html', {'form': form})

def login_view(request):
    form = LoginForm(request.POST or None)
    message = ''
    
    if request.method == 'POST':
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=email, password=password)
            
            if user is not None:
                login(request, user)
                return redirect('home')  # Redirect after login
            else:
                message = 'Invalid email or password'
    
    return render(request, 'traco/login.html', {'form': form, 'message': message})

def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            User.objects.create_user(
                username=form.cleaned_data['email'],
                first_name=form.cleaned_data['name'],
                email=form.cleaned_data['email'],
                password=form.cleaned_data['password']
            )
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'traco/register.html', {'form': form})

# accounts/views.py


from .utils import generate_otp, send_otp_email
from .forms import VerifyOtpForm
import random

# Step 1: Send OTP
def send_otp_view(request):
    if request.method == "POST":
        form = PartnerForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data["email"]

            # Generate OTP
            otp = generate_otp()

            # Send OTP via email
            send_otp_email(email, otp)

            # Save data in session
            request.session["otp"] = otp
            request.session["partner_data"] = form.cleaned_data

            # Redirect to OTP verification
            return redirect("verify_otp")
    else:
        form = PartnerForm()

    return render(request, "traco/partner.html", {"form": form})


# Step 2: Verify OTP
def verify_otp_view(request):
    success_message = None
    if request.method == "POST":
        form = VerifyOtpForm(request.POST)
        if form.is_valid():
            otp_entered = form.cleaned_data["otp"]
            otp_saved = request.session.get("otp")

            if otp_entered == otp_saved:
                success_message = "✅ OTP verified! You are now a TRACO partner."
            else:
                messages.error(request, "❌ Invalid OTP, try again.")
    else:
        form = VerifyOtpForm()

    return render(request, "traco/verify_otp.html", {
        "form": form,
        "success_message": success_message
    })
