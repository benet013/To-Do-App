from django.shortcuts import render,redirect
from .forms import UserRegisterForm
from django.contrib import messages
from django.contrib.auth.views import LoginView,LogoutView

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created from {username}')
            return redirect('todo-home')
    else:
        form = UserRegisterForm()    
    
    return render(request, 'user/register.html', {'form':form})

class CustomLoginView(LoginView):
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('todo-home')
        
        return super().dispatch(request, *args, **kwargs)


class CustomLogoutView(LogoutView):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login')
        
        return super().dispatch(request, *args, **kwargs)
    