from django.shortcuts import render, redirect
from django.contrib import messages
from loginapp.models import User
from .models import Message, Comment
import bcrypt

def home(request):
    
    if 'loggedinID' in request.session:
        loggedIn= request.session['loggedinID']
        loggedInEmail= User.objects.get(id=loggedIn).email
        loggedInObj= User.objects.get(id=loggedIn)
    else:
        loggedIn='guest'
        loggedInEmail='guestmail'
        # UsersPosts = Message.objects.get( id = loggedIn)
    allposts = Message.objects.all()
    context = {
        'loggedIn':loggedIn,
        'loggedInEmail':loggedInEmail,
        'loggedInObj':loggedInObj,
        'allposts':allposts
    }
    return render(request, 'home.html', context)

def newlogout(request):
    request.session.clear()
    return redirect('/')

def addPost(request, user_id):
    if 'loggedinID' in request.session:
        loggedIn= request.session['loggedinID']
        loggedInObj= User.objects.get(id=loggedIn)
    else:
        loggedIn='guest'
    print(request.POST)
    Message.objects.create(user_id = loggedInObj, content = request.POST['message'])
    return redirect('/wall')

def deletePost(request, post_id):
    print(request.POST)
    Message.objects.get(id = post_id).delete()
    return redirect('/wall')

def addComment(request, post_id):
    if 'loggedinID' in request.session:
        loggedIn = request.session['loggedinID']
        loggedInObj = User.objects.get(id=loggedIn)
    else: loggedIn = 'guest'
    thisPost = Message.objects.get(id = post_id)
    print(request.POST)
    Comment.objects.create(message_id = thisPost , user_id = loggedInObj, content= request.POST['comment'])
    return redirect('/wall')

def deleteComment(request, comment_id):
    print(request.POST)
    Comment.objects.get(id = comment_id).delete()
    return redirect('/wall')