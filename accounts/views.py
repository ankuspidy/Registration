from django.contrib.auth import login as auth_login
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from .forms import RegistrationForm
from django.contrib.auth.decorators import login_required
from .models import Gallery

def signup(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()

            return redirect('login')
    else:
        form = RegistrationForm()
    return render(request, 'signup.html', {'form': form})


def home(request):
    if(request.method == 'POST'):
        if(request.user.is_authenticated):
            if('upload' in request.POST):
                usr = request.user
                new_img = Gallery.objects.create(user = usr, image = request.FILES[ 'file'])
                new_img.save()
                return redirect('home')

            if('Edit' in request.POST):
                usr = request.user
                a = Gallery.objects.get(id = request.POST['Edit'],user = usr)
                print(request.FILES)
                a.delete()
                new_img = Gallery.objects.create(user = usr, image = request.FILES[ 'file'])
                new_img.save()
                return redirect('home')

            if('Delete' in request.POST):
                usr = request.user
                a = Gallery.objects.get(id = request.POST['Delete'], user = usr)
                a.delete()
                return redirect('home')
        else:
            return redirect('login')
    pic = Gallery.objects.all()
    if(request.user.username):
        user = User.objects.filter(username = request.user.username).get()
        return render(request, 'home.html',{'user':user,'pic':pic})
    return render(request, 'home.html',{'pic':pic})


def about(request):

    return render(request, 'about.html',{'user':request.user.username})
