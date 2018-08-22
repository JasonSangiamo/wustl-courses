from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.contrib.auth.forms import (
    AuthenticationForm, PasswordChangeForm, PasswordResetForm, SetPasswordForm,
)
from django.contrib import messages
from django.http import HttpResponseRedirect, QueryDict
from django.utils.http import is_safe_url
from django.shortcuts import resolve_url
from django.conf import settings
from django.contrib.auth import (
    REDIRECT_FIELD_NAME, get_user_model, login as auth_login,
    logout as auth_logout, update_session_auth_hash,
)
from django.contrib.sites.shortcuts import get_current_site
from django.template.response import TemplateResponse

def home(request, template_name='home/home.html',
          authentication_form=AuthenticationForm,):
    redirect_field_name = 'home'
    redirect_to = request.POST.get(redirect_field_name,
                                   request.GET.get(redirect_field_name, ''))
    # redirect authenticated users to departments page
    if request.user.is_authenticated:
        return HttpResponseRedirect('courses')

    if request.method == 'POST':
        if 'signup' in request.POST:
            signup_form = UserCreationForm(request.POST)
            if signup_form.is_valid():
                signup_form.save()
                username = signup_form.cleaned_data.get('username')
                raw_password = signup_form.cleaned_data.get('password1')
                user = authenticate(username=username, password=raw_password)
                login(request, user)
                return redirect('departments')
            else:
                messages.warning(request,
                                 'There was an issue registering your account. Please confirm you entered in all fields correctly!')
        if 'login' in request.POST:
            # taken from https://docs.djangoproject.com/en/1.8/_modules/django/contrib/auth/views/
            


            form = authentication_form(request, data=request.POST)
            if form.is_valid():

                # Ensure the user-originating redirection url is safe.
                if not is_safe_url(url=redirect_to, host=request.get_host()):
                    redirect_to = resolve_url(settings.LOGIN_REDIRECT_URL)

                # Okay, security check complete. Log the user in.
                auth_login(request, form.get_user())

                return HttpResponseRedirect(redirect_to)
            else:
                messages.warning(request,
                                 'There was an issue logging into your account. Please confirm you entered in all fields correctly!')
    signup_form = UserCreationForm()
    login_form = AuthenticationForm()
    current_site = get_current_site(request)
    return TemplateResponse(request, 'home/home.html',
                            {'signup_form': signup_form, 'login_form': login_form, 'current_site': current_site,
                             'site_name': current_site.name,})