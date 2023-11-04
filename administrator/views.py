from django.shortcuts import render, redirect
from django.contrib import messages,auth
from django.contrib.auth.models import User
from .models import UserProfile
from django.contrib.admin.models import LogEntry
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from administrator.models import Item
from django.core.paginator import Paginator, EmptyPage

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
def next(request):
    try:
        next=request.META['PATH_INFO']
    except:
        next='/'
    return next

def profile(request):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            activity=LogEntry.objects.filter(user_id=request.user.id)[:20]
            data=list(activity.values())
            context={
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
    nxt=next(request)
    if request.user.is_authenticated:
        if request.user.is_superuser:
            context={
            }
            return render(request, 'admins/dashboard.html', context)
        else:
            return redirect('/')
    else:
        next_str=f"/login?next={nxt}"
        return redirect(next_str)
    


def orders(request):
    nxt=next(request)
    if request.user.is_authenticated:
        if request.user.is_superuser:
            context={
            }
            return render(request, 'admins/orders.html', context)
        else:
            return redirect('/')
    else:
        next_str=f"/login?next={nxt}"
        return redirect(next_str)
    


def new(request):
    try:
        action=request.GET['action']
        id=request.GET['id']
    except:
        action = None
        id=None
    if request.method == 'POST':
        title=request.POST['title']
        available=request.POST['available']
        price1=request.POST['price1']
        price2=request.POST['price2']
        trending=request.POST['trending']
        offer=request.POST['offer']

        if action is not None and id is not None:
            if action == 'delete':
                print("Deleted")
            else:
                print("Editing")
        else:
            pass
    context={
    }
    return render(request, 'admins/new.html', context)

def edit(request):
    nxt=next(request)
    try:
        q=request.GET['q']
    except:
        q=None
    if request.user.is_authenticated:
        if request.user.is_superuser:
            if q is not None:
                result=Item.objects.filter(title__icontains=q, outofstalk='False')
                page_n=request.GET.get('page',1)
                p=Paginator(result, 10)
                try:
                    items=p.page(page_n)
                except EmptyPage:
                    items=p.page(1)
            else:
                items=Item.objects.all()
            context={
                'items':items,
                'q':q,
            }
            return render(request, 'admins/edit.html', context)
        else:
            return redirect('/')
    else:
        next_str=f"/login?next={nxt}"
        return redirect(next_str)

def blog(request):
    nxt=next(request)
    if request.user.is_authenticated:
        if request.user.is_superuser:
            if request.method=='POST':
                title=request.POST['title']
                img=request.POST['img']
                body=request.POST['body']
                # Hello World
            else:
                context={
                }
                return render(request, 'admins/blog.html', context)
        else:
            return redirect('/')
    else:
        next_str=f"/login?next={nxt}"
        return redirect(next_str)
    
    
