from django.shortcuts import render, redirect
from .forms import SignupForm, EditProfileForm, UserProForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.models import User
from django.http import JsonResponse

from .models import Userpro


# Create your views here.


def index(request):
    return render(request, 'app/dashboard.html', {})


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            new_user = authenticate(username=form.cleaned_data['username'],
                                    password=form.cleaned_data['password1'],
                                    )
            login(request, new_user)
            return redirect('/update/')
        else:
            return render(request, 'app/signup.html', {'form': form})
    else:
        form = SignupForm()
        args = {'form': form}
        return render(request, 'app/signup.html', args)


def edit(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = EditProfileForm(instance=request.user)
        return render(request, 'app/info.html', {'form': form})


def cp(request):
    a = False
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            a = False
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('/')
        else:
            a = True
            return render(request, 'app/changepassword.html', {'a': a, 'form': 'form'})
    else:
        form = PasswordChangeForm(user=request.user)
        return render(request, 'app/changepassword.html', {'form': form})


# def update(request):
#     if request.method == 'POST':
#         form = UserProForm(request.POST or None)
#         if form.is_valid():
#             form.save()
#             return redirect('/')
#         else:
#             redirect('/')
#     else:
#         form = UserProForm()
#         return render(request, 'app/update.html', {'form': form})

def update(request):
    if request.method == 'POST':
        form = UserProForm(request.POST or None, request.FILES)
        print(request)
        # obj = Userpro.objects.filter(user=request.user)
        # print(request)
        # print("object is", obj[0].country)
        if form.is_valid():
            form.save()
            return redirect('/')
        # elif len(obj)!=0:

        else:
            # obj = Userpro.objects.filter(user=request.user.username)
            # print(obj[0])
            return redirect('/update/')
    else:
        form = UserProForm({'user': request.user})
        return render(request, 'app/update.html', {'form': form})


def validate_username(request):
    username = request.GET.get('username', None)
    data = {
        'is_taken': User.objects.filter(username__iexact=username).exists()
    }
    return JsonResponse(data)


def dashboard(request):
    return render(request, 'app/dashboard.html', {})


def problems(request):
    return render(request, 'app/problems.html', {})


def contest(request):
    return render(request, 'app/contest.html', {})


def leaderboard(request):
    return render(request, 'app/leaderboard.html', {})


def contribute(request):
    return render(request, 'app/contibute.html', {})


def statistics(request):
    return render(request, 'app/statistics.html', {})


def discuss(request):
    return render(request, 'app/discuss.html', {})
