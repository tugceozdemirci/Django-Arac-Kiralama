from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

# Create your views here.
from car.models import Category, Reservation, Car
from home.models import UserProfile
from user.forms import UserUpdateForm, ProfileUpdateForm


def index(request):
    category = Category.objects.all()
    current_user = request.user
    profile = UserProfile.objects.get(user_id=current_user.id)
    context = {
        'category': category,
        'profile': profile,
    }
    return render(request, 'user_profile.html', context)


@login_required(login_url='/login')
def user_update(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.userprofile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Hesabınız Başarıya Güncellendi!')
            return redirect('/user')
    else:
        category = Category.objects.all()
        current_user = request.user
        profile = UserProfile.objects.get(user_id=current_user.id)
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.userprofile)
        context = {
            'category': category,
            'user_form': user_form,
            'profile_form': profile_form,
            'profile': profile
        }
        return render(request, 'user_update.html', context)


@login_required(login_url='/login')
def change_password(request):
    current_user = request.user
    profile = UserProfile.objects.get(user_id=current_user.id)
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Şifreniz Başarıyla Güncellendi !')
            return redirect('change_password')
        else:
            messages.warning(request, 'Lütfen Aşağıdaki Hatayı Düzeltin.<br>' + str(form.errors))
            return HttpResponseRedirect('/user/password')
    else:
        category = Category.objects.all()
        form = PasswordChangeForm(request.user)

        return render(request, 'change_password.html', {
            'form': form, 'category': category, 'profile': profile
        })


@login_required(login_url='/login')
def reservation(request):
    category = Category.objects.all()
    current_user = request.user
    profile = UserProfile.objects.get(user_id=current_user.id)
    reservation = Reservation.objects.filter(user_id=current_user.id)
    context = {
        'category': category,
        'reservation': reservation,
        'profile': profile,
    }
    return render(request, 'user_reservation.html', context)


@login_required(login_url='/login')
def udelete_reservation(request, id):
    Car.objects.get(pk=id)
    current_user = request.user
    Reservation.objects.filter(id=id, user_id=current_user.id).delete()
    messages.success(request, 'Rezervasyonunuz Silindi.')
    return HttpResponseRedirect('/user/reservation')


@login_required(login_url='/login')
def uadd_reservation(request, id):
    car = Car.objects.get(pk=id)
    current_user = request.user
    profile = UserProfile.objects.get(user_id=current_user.id)
    category = Category.objects.all()
    reservation = Reservation.objects.filter(user_id=current_user.id)
    context = {
        'category': category,
        'reservation': reservation,
        'profile': profile,
        'car': car,
    }
    return render(request, 'add_reservation.html', context)
