from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login
from django.db.models import Q
from core.models import Commande_Menu, Menu, Plats, Commande_Plat, Pofile
from .forms import SignUpForm
from django.contrib.auth import logout
from django.contrib import messages
# Create your views here.


def Home(request):
    menu = Menu.objects.all()
    plat = Plats.objects.all()
    try:
        profile = Pofile.objects.get(user=request.user)
    except:
        profile= None
    dict = {
        'menu':menu,
        'plat':plat,
        'profile':profile,
    }
    return render(request , 'index.html' , dict)



def Signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  
            # load the profile instance created by the signal
            user.save()
            raw_password = form.cleaned_data.get('password1')
            # login user after signing up
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            #create profile
            Pofile.objects.create(
                user = request.user
            )
            # redirect user to home page
            messages.success(request, 'Your account is ceated successfully!')
            return redirect('dashboard')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})



def commande_menu(request):
    if request.method == 'POST':
        menu_name = request.POST.get('menu')
        menu_instance = Menu.objects.get(title=menu_name)
        Commande_Menu.objects.create(
            user=request.user,
            menu=menu_instance,
        )
        messages.success(request, 'We receive your order succesfuly, thank for your trust')

    return redirect(Home)

def commande_plat(request):
    if request.method == 'POST':
        plat_name = request.POST.get('plat')
        plat_instance = Plats.objects.get(title=plat_name)
        Commande_Plat.objects.create(
            user=request.user,
            plat=plat_instance,
        )
        messages.success(request, 'We receive your order succesfuly, thank for your trust')
    return redirect(Home)

def search(request):
    query = request.GET.get("q")
    plat = Plats.objects.filter(
    Q(title__icontains=query)
    )
    dict = {
        'plat':plat,
    }
    return render (request , 'search.html', dict)

def dashboard(request):
    profile = Pofile.objects.get(user=request.user)
    menu_order = Commande_Menu.objects.filter(user=request.user)
    plat_order = Commande_Plat.objects.filter(user=request.user)
    plat = Plats.objects.all()
    
    dict={
        'profile':profile,
        'menu_order':menu_order,
        'plat_order':plat_order,
        'plat':plat,
    }
    return render(request, 'dashboard.html', dict)

def Edit_profile(request):
    profile = Pofile.objects.get(user=request.user)
    if request.method == 'POST':
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        address_1 = request.POST.get('address_line_1')
        address_2 = request.POST.get('address_line_2')
        profile.email = email
        profile.phone = phone
        profile.address_1 = address_1
        profile.address_2 = address_2
        profile.save()
        messages.info(request, 'Your profile informations was update successfuly')

    return redirect (dashboard)

def logout_view(request):
    logout(request)
    messages.success(request, 'you logout successfuly')

    return redirect('login')