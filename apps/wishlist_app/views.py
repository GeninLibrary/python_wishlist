from django.shortcuts import render,redirect
from django.contrib import messages
from ..login_app.models import User
from models import Item
import datetime
from time import gmtime,strftime                                    # TO CHANGE BACK STRFTIME DATE STORED IN USER OBJECT AND ITEM OBJECT



def logout(request):
    request.session.flush()                                 #LOGS OUT
    return redirect('/')

def main(request):  
    if 'name' not in request.session:                              #will not load if not logged in,
        return redirect('/')
    context = {
        'this_user' : User.objects.get(id = request.session['id']),
        'other_items' : Item.objects.exclude(all_users = User.objects.get(id = request.session['id']))
    }  
                                      # RENDERS LOGIN PAGE
    return render(request, 'wishlist_app/main.html', context)


def render_item_build(request):
    if 'name' not in request.session:                              #will not load if not logged in,
        return redirect('/')                                        # RENDERS LOGIN PAGE
    return render(request, 'wishlist_app/item_build.html')


def add_item(request):
    results = Item.objects.validateItem(request.POST)

    if results['status'] == False:                                              # IF ITEM NAME INVALID
        for error in results['errors']:
            messages.success(request,error)
            return redirect ('/render_item_build')
    else:
        x = User.objects.get(id = request.POST['session_user'])                                                     # ELSE CREATE ITEM AND ADD USER TO CREATOR FOREIGN KEY
        y = Item.objects.create(name = request.POST['name'], date = request.session['date'], creator = x)                   

        y.all_users.add(x)
        y.save()
        return redirect('/main')                                                               
        
    return redirect('/main')

def delete_item(request, item_id):
    deleted = Item.objects.get(id = item_id)
    deleted.delete()

    return redirect('/main')

def display_item(request, item_id):
    if 'name' not in request.session:                              #will not load if not logged in,
        return redirect('/')
    context = {
        'shown_item' : Item.objects.get(id = item_id)
    }
    return render(request, 'wishlist_app/item_display.html', context)

def add_to_wishlist(request, item_id):
    x = User.objects.get(id = request.session['id'])
    y = Item.objects.get(id = item_id)

    x.all_items.add(y)
    x.save()

    return redirect('/main')


