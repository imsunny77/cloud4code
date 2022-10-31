from django.shortcuts import render,redirect
from administration.forms import *
from django.views.generic import UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

def home(request):
    if request.user.is_authenticated:
        rootuser_list =RootUser.objects.all()
        return render(request,'administration/home.html',{'rootuser_list':rootuser_list})
    else:
        return redirect('login')
        
def add_user(request):
    form = SignUpForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('login')
    return render(request,'registration/sign_up.html',{'form':form})

class UserUpdate(LoginRequiredMixin, UpdateView):
    model = RootUser
    form_class =RootUserForm
    success_url = reverse_lazy('administration:home') 

class UserDetail(LoginRequiredMixin, DetailView):
    model = RootUser

def delete_user(request,pk):
    user = RootUser.objects.get(pk=pk)
    user.delete()
    return redirect('administration:home')