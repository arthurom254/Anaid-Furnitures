from django.shortcuts import render, redirect
from django.contrib import messages,auth
from django.contrib.auth.models import User
from .models import UserProfile, Category, Description, ItemImg
from django.contrib.admin.models import LogEntry
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from administrator.models import Item
from django.core.paginator import Paginator, EmptyPage
from django.http import HttpResponse
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
        productImg=None
        if 'img' in request.FILES:
            img=request.FILES.getlist('img')
            try:
                img1=img[0]
                img2=img[1]
                img3=img[2]
                img4=img[3]
                productImg=ItemImg.objects.create(title=title)
                productImg.img=img1
                productImg.img1=img2
                productImg.img2=img3
                productImg.img3=img4
                productImg.save()
            except:
                messages.info(request,'Image Error: ensure you use 4 images')
                return redirect(next(request))
        category=request.POST.getlist('category')
        description_h=request.POST.getlist('description_h')
        description_b=request.POST.getlist('description_b')

        if trending == '1':
            trending='True'
        else:
            trending='False'
        

        if offer == '1':
            offer='True'
        else:
            offer='False'
        try:
            item=Item.objects.create(title=title,price=price1,img=productImg, price2=price2, available=available, offer=offer, trending=trending )
        except:
            try:
                item=Item.objects.get(title=title)
                item.price=price1
                item.price2=price2
                if productImg is not None:
                    item.img=productImg
                item.available=available
                item.offer=offer
                item.trending=trending
                item.category.clear()
                item.description.clear()
                print("Save")
            except:
                messages.info(request, "Cannot create this product.")
                return redirect(next(request))
        for c in category:
            category=Category.objects.get(id=c)
            item.category.add(category)
        for index,d_head in enumerate(description_h):
            desc, c=Description.objects.get_or_create(title=d_head, body=description_b[index])
            item.description.add(desc)
        print("Item is ", item)
        item.save()
        return HttpResponse(f"{category} then id is {id} : head-{description_h} body-{description_b}")
        
    else:
        if action is not None and id is not None:
            item=Item.objects.get(id=id) #Or 404
        else:
            item=None
        context={
            'item':item
            
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
                result=Item.objects.all()
                page_n=request.GET.get('page',1)
                p=Paginator(result, 10)
                try:
                    items=p.page(page_n)
                except EmptyPage:
                    items=p.page(1)
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
    
    
