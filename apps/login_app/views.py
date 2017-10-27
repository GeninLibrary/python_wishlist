# LOGIN APP --- VIEWS

from django.shortcuts import render,redirect
from django.contrib import messages
from models import User



def login_page(request):                                        # RENDERS LOGIN PAGE
    return render(request, 'login_app/login.html')


def register_account(request):                                  # RECIEVES RESULTS FROM REGISTER_VAL()    
    results = User.objects.registerVal(request.POST)           # IF "TRUE" THEN CREATE OBJECT
                                                                # IF "FALSE" THEN DISPLAY ERROR MESSAGE
    if results['status'] == False:
        for error in results['errors']:
            messages.success(request,error)
    else: 
        User.objects.createUser(request.POST)
        messages.success(request, "You now have an account...nice.")
    return redirect('/')    



def login(request):                                             # RECIEVES RESULTS FROM LOGIN_VAL()
    
    results = User.objects.loginVal(request.POST)               # IF "TRUE" THEN REDIRECT TO SUCCESSFUL LOGIN       
                                                                # IF "FALSE" THEN REDIRECT TO "/" AND DISPLAY ERROR
    if results['status'] == False:
        for error in results['errors']:
            messages.success(request,error)
            return redirect ('/')
    else:
        request.session['name'] = results['retrieved_account'].name     # RETRIEVED ACCOUNT IS THE LOGIN ACCOUNT
        request.session['id'] = results['retrieved_account'].id                     # STORE OBJECT "ID" IN SESSION                      
        request.session['date'] = results['retrieved_account'].date
        return redirect('/main')                                                                   
                                # REDIRECT TO SECOND APP                                                  
                                            

