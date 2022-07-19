from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout

# Create your views here.
def home(request):
    return render(request,"authentication/index.html")


    
def signup(request):

    if request.method == "POST":
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        password = request.POST['password']
        confirm = request.POST['confirm']

        myuser = User.objects.create_user(username,email,password)
        myuser.first_name=fname
        myuser.last_name=lname
        myuser.save()

        messages.success(request,"Your account has been successfully created.")
        return redirect('signin')

    return render(request,"authentication/signup.html")





def signin(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user=authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            fname = user.first_name
            return render(request,"authentication/index.html",{'fname':fname})
        else:
            messages.error(request,"Bad credentials")
            return redirect('home')

    return render(request,"authentication/signin.html")




def signout(request):
    logout(request)
    messages.success(request,"Logged out Sucessfully!")
    return redirect('home')

