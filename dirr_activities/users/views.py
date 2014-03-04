from django.template import RequestContext
from django.shortcuts import render
from users.forms import LoginForm
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate
from django.contrib.auth import logout
from django.contrib.auth import login


def login(request):
    #if request.user.is_authenticated():
        #return HttpResponseRedirect(reverse('main:main'))
    #else:
    next_url = "?next=/main/"
    form = LoginForm(next=next_url)
    dictionary = {'form': form, 'next': next_url}

    return render('users/login.html', dictionary)


def authenticate_view(request, next_url):
    user_username = request.POST['username']
    user_password = request.POST['password']
    user = authenticate(username=user_username, password=user_password)
    if user is not None:
        login(request, user)
        return HttpResponseRedirect(next_url)
    else:
        return HttpResponseRedirect('/login/failed?next=' + next_url)


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('users:login'))