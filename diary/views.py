from django.shortcuts import render, redirect
from .models import PhotoEntry
from .forms import PhotoEntryForm
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    photos=PhotoEntry.objects.filter(user=request.user).order_by('-date_uploaded')
    dates=photos.values_list('date_uploaded', flat=True).distinct()
    grouped_photos={date:photos.filter(date_uploaded=date) for date in dates}
    return render(request,'diary/home.html',{'grouped_photos':grouped_photos})

@login_required
def upload_photo(request):
    if request.method=='POST':
        form=PhotoEntryForm(request.POST, request.FILES)
        if form.is_valid():
            photo_entry=form.save(commit=False)
            photo_entry.user=request.user
            photo_entry.save()
            return redirect('home')
    else:
        form = PhotoEntryForm()
    return render(request,'diary/upload.html',{'form': form})

from django.contrib.auth import login
from .forms import RegisterForm

def register(request):
    if request.method=="POST":
        form=RegisterForm(request.POST)
        if form.is_valid():
            user=form.save()
            login(request,user) 
            return redirect('home')
    else:
        form=RegisterForm()
    return render(request,'diary/register.html',{'form': form})

