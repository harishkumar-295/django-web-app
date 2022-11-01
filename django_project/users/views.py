from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import RegisterUserForm

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,f'Account Created for user {username}')
            return redirect('blog-home')
    else:
        form = RegisterUserForm()
    return render(request, 'users/register.html',{'form':form})
