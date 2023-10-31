from django.shortcuts import render, redirect
from django.contrib import messages,auth
from django.contrib.auth.models import User
from .models import UserProfile
from django.contrib.admin.models import LogEntry
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def login(request):
    if request.method=='POST':
        username=request.POST['email']
        password=request.POST['pwd']
        user=auth.authenticate(username=username, password=password)
        try:
            next=request.GET['next']
        except:
            next='/'
        if user is not None:
            auth.login(request, user)
            return redirect(f'{next}')
        else:
            messages.info(request, 'Invalid credentials')
            return redirect(f'/login?next={next}')

    else:
        if request.user.is_authenticated:
            return redirect('/')
        else:
            # messages.info(request, 'Log in')
            return render(request, 'clients/login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

        
def signup(request):
    if request.method == 'POST':
        fname=request.POST['fname']
        lname=request.POST['lname']
        email=request.POST['email']
        password=request.POST['pwd']
        password2=request.POST['pwd2']

        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request,'Email already used')
                return redirect(signup)
            else:
                user=User.objects.create_user(username=email, email=email, password=password, first_name=fname, last_name=lname)
                user.save()
                return redirect(login)
        else:
            
            messages.info(request,'Password not same')
            return redirect(signup)
    else:
        if request.user.is_authenticated:
            return redirect('/')
        else:
            # messages.info(request,'Create your account')
            return render(request, 'clients/signup.html') 

def profile(request):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            activity=LogEntry.objects.filter(user_id=request.user.id)[:20]
            person=UserProfile.objects.get(user=User(id=request.user.id))
            data=list(activity.values())
            context={
                'person':person,
                'activity':activity,
            }
            messages.success(request, "Welcome Back")
            # return JsonResponse(data, safe=False)
            return render(request, 'admins/profile.html', context)
        else:
            messages.info(request, 'You are redirected to this page becaue admin only page')
            return redirect('/')
    else:
        return redirect(login)


def dashboard(request):
    person=UserProfile.objects.get(user=User(id=request.user.id))
    context={
        'person':person,
    }
    return render(request, 'admins/dashboard.html', context)


def orders(request):
    person=UserProfile.objects.get(user=User(id=request.user.id))
    context={
        'person':person,
    }
    return render(request, 'admins/orders.html', context)


def new(request):
    person=UserProfile.objects.get(user=User(id=request.user.id))
    context={
        'person':person,
    }
    return render(request, 'admins/new.html', context)

def edit(request):
    person=UserProfile.objects.get(user=User(id=request.user.id))
    context={
        'person':person,
    }
    return render(request, 'admins/edit.html', context)

