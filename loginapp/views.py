from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User
import bcrypt

# Create your views here.

def index(request): 
      
    context = {
        'allUsers': User.objects.all()
        # 'loggedin' : loggedinUser
        # 'currentUser': loggedinUser
    }
    return render(request, "index.html", context)

def login(request):
    print(request.POST) 
    loginerrors = User.objects.loginValidator(request.POST)
    print(loginerrors)
    if len(loginerrors) > 0:
        for key, value in loginerrors.items():
            messages.error(request, value)
        return redirect('/')
    else:
        loggedUser = User.objects.filter(email = request.POST['email'])[0]
        print('PRINTING A LIST OF USER OBJECTS THAT MATCH THE LOGIN FORM EMAIL')
        print('loggedUser')
        request.session['loggedinID'] = loggedUser.id
        return redirect('/success')

def logout(request):
    request.session.clear()
    return redirect('/')

def register(request):
    print(request.POST)
    errors = User.objects.reg_validator(request.POST)
    
    print('errors', errors)
    if len(errors) > 0:
        for key, val in errors.items():
            messages.error(request, val)
        print('failed to update')
        return redirect('/')
    else:
        securepass = bcrypt.hashpw(request.POST['pw'].encode(), bcrypt.gensalt()).decode()  
        print(securepass)
        newUser = User.objects.create(first_name = request.POST['firstName'],
                            last_name = request.POST['lastName'],
                            email = request.POST['email'],
                            password = securepass)
        request.session['loggedinID'] = newUser.id
        return redirect('/success')

def success(request):
    if 'loggedinID' not in request.session:
        return redirect('/')
    loggedinUser = User.objects.get(id= request.session['loggedinID'])
    context = {
        'loggedin' : loggedinUser
    }
    return render(request, 'success.html', context)

def destroy(request, user_id):
    User.objects.get(id=user_id).delete()
    return redirect('/')
