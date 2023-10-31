# This is a complete serch that returns the items specified in the get['q']
from django.http import HttpResponse
from administrator.models import Item
from django.shortcuts import render, redirect
from django.contrib import messages
def search_item(request):
    try:
        q=request.GET['q']
        item=Item.objects.filter(title__icontains=q, outofstalk='False')
        context={
            'item':item,
        }
        if len(q.strip()) == 0:
            messages.info(request,"Cannot Make an empty search")
            return redirect('/')
        else:
            return render(request, 'clients/search.html', context)
    except:
        messages.info(request,"Cannot Make an empty search")
        return redirect('/')