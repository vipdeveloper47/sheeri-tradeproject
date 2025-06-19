from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from .models import UserProfile
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt, csrf_protect


@login_required(login_url='login')
def index(request):
    return render(request, 'core/pak-traders.html')

@csrf_exempt
def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        key = request.POST.get('key')
        agree = request.POST.get('agree') == 'on'

        # Validate that all required fields are present.
        if not all([username, email, password, confirm_password, key, agree]):
            messages.error(request, "All fields and terms agreement are required.")
            return redirect('register')

        if password != confirm_password:
            messages.error(request, "Passwords do not match.")
            return redirect('register')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already taken.")
            return redirect('register')

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already registered.")
            return redirect('register')

        try:
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()

            UserProfile.objects.create(
                user=user,
                key=key,
                email=email,
                password=password,
                confirm_password=confirm_password,
                terms_accepted=True
            )
            print(f"username={username}, email={email}, password={password}, key={key}, agree={agree}")


            messages.success(request, "Account created successfully.")
            return redirect('login')
        except Exception as e:
            messages.error(request, f"Signup failed: {str(e)}")
            return redirect('register')

    return render(request, 'core/login.html')

@csrf_exempt
def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            messages.success(request, 'Successfully logged in!')
            return redirect('pak_traders')  
        else:
            messages.error(request, 'Invalid username or password.')
            return redirect('login')

    return render(request, 'core/login.html') 

@require_POST
@csrf_protect
def logout_view(request):
    logout(request)
    messages.success(request, "You have been logged out.")
    return redirect("login")


@login_required(login_url='login')
def pak_traders_view(request):
    return render(request, 'core/pak-traders.html')  


@login_required
def ai_predictor(request):
    return render(request, 'core/ai-predictor.html') 