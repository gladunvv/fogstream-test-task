from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.views.generic import TemplateView
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class SignUpView(TemplateView):

    template_name = 'accounts/signup.html'

    def get(self, request, *args, **kwargs):
        form = UserCreationForm()
        context = {
            'form': form,
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('accounts:login')
        context = {
            'form': form,
        }
        return render(request, self.template_name, context)


class LogInView(TemplateView):

    template_name = 'accounts/login.html'

    def get(self, request, *args, **kwargs):
        form = AuthenticationForm()
        context = {
            'form': form,
        }
        return render(request, self.template_name, context)


    def post(self, request, *args, **kwargs):
        form = AuthenticationForm(request, data=request.POST)
        username = request.POST.get('username')
        password = request.POST.get('password')
        if form.is_valid():
            user = authenticate(
                request,
                username=username, 
                password=password
                )
        if user is not None:
            login(request, user)
            return redirect('')
        else:
            messages.error(request, 'Bad username or password.')
        return redirect('accounts:login')


class LogOutView(TemplateView):
    def get(self, request):
        logout(request)
        return redirect('accounts:login')
