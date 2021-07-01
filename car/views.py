from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect

from car.models import ReservationForm, Reservation


def index(request):
    return HttpResponse("Car Page")


@login_required(login_url="/login")
def addreservation(request, id):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            current_user = request.user

            data = Reservation()
            data.user_id = current_user.id
            data.car_id = id
            data.name = form.cleaned_data['name']
            data.email = form.cleaned_data['email']
            data.phone = form.cleaned_data['phone']
            data.location = form.cleaned_data['location']
            data.days = form.cleaned_data['days']
            data.checkin = form.cleaned_data['checkin']
            data.checkout = form.cleaned_data['checkout']
            data.ip = request.META.get('REMOTE_ADDR')
            data.save()
            messages.success(request, 'Rezervasyon Kaydınız Başarıyla Alınmıştır. İyi yolculuklar dileriz! ')
            return HttpResponseRedirect('/user/reservation/')

    messages.warning(request, 'Rezervasyon Kaydınız Yapılamadı. Lütfen Bilgilerinizi Kontrol Ediniz! ')
    return HttpResponseRedirect('/user')
