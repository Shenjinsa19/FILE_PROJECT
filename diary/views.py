from django.shortcuts import render, redirect
from .models import PhotoEntry
from .forms import PhotoEntryForm
from django.contrib.auth.decorators import login_required
from django.utils.timezone import localtime


# @login_required
# def home(request):
#     photos=PhotoEntry.objects.filter(user=request.user).order_by('-date_uploaded')
#     dates=photos.values_list('date_uploaded', flat=True).distinct()
#     grouped_photos={date:photos.filter(date_uploaded=date) for date in dates}
#     return render(request,'diary/home.html',{'grouped_photos':grouped_photos})

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




from django.views.generic.edit import UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

class PhotoEntryUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model=PhotoEntry
    fields=['photo', 'caption']
    template_name='diary/photo_edit.html'
    success_url=reverse_lazy('home')
    def test_func(self):
        return self.request.user==self.get_object().user


class PhotoEntryDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model=PhotoEntry
    template_name='diary/photo_delete.html'
    success_url=reverse_lazy('home')
    def test_func(self):
        return self.request.user==self.get_object().user






#pagination

from django.core.paginator import Paginator
from collections import defaultdict
from django.core.paginator import Paginator
@login_required
def home(request):
    photos = PhotoEntry.objects.filter(user=request.user).order_by('-date_uploaded')
    paginator = Paginator(photos, 2) 
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    grouped_photos = {}
    for photo in page_obj:        #in each page display by -date
        date_str = photo.date_uploaded.date().strftime('%Y-%m-%d')
        grouped_photos.setdefault(date_str, []).append(photo)
    context = {
        'grouped_photos': grouped_photos,
        'page_obj': page_obj,
    }
    return render(request, 'diary/home.html', context)


