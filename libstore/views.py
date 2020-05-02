from .models import library_manager
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from . import forms

# Create your views here.

app_name = 'libstore'

@login_required(login_url='/accounts/login/')
def library(request):
    books = library_manager.objects.all()
    context = {'book': books}
    return render(request, 'libstore/library.html', context)

@login_required(login_url='/accounts/login/')
def shelf(request,slug):
    book = library_manager.objects.get(slug=slug)
    return render(request, 'libstore/detailed_book.html', {'book': book})

@login_required(login_url='/accounts/login')
def create_book(request):
    if request.method == 'POST':
        form = forms.Createlib(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()

            return redirect('libstore:library')
    else:
        form = forms.Createlib()
    return render(request, 'libstore/createBook.html', {'form': form})

@login_required(login_url='accounts/login')
def download(request,file_name):
    
    f = library_manager.objects.get(stored_file=file_name)

    

