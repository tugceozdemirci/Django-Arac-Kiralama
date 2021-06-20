from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from car.models import Car, Category
from home.models import Setting, ContactFormu, ContactFormMessage


def index(request):
    setting = Setting.objects.get(pk=1)
    sliderdata = Car.objects.all()[:2]
    category = Category.objects.all()
    daycars = Car.objects.all()[:3]
    lastcars = Car.objects.all().order_by('-id')[:3]
    randomcars = Car.objects.all().order_by('?')[:3]
    context = {'setting': setting,
               'category': category,
               'page': 'home',
               'sliderdata': sliderdata,
               'daycars': daycars,
               'lastcars': lastcars,
               'randomcars': randomcars,
               }
    return render(request, 'index.html', context)


def hakkimizda(request):
    setting = Setting.objects.get(pk=1)
    category = Category.objects.all()
    context = {'setting': setting ,
               'category': category,
               'page':'hakkimizda',
               }
    return render(request, 'hakkimizda.html', context)


def referanslar(request):
    setting = Setting.objects.get(pk=1)
    category = Category.objects.all()
    context = {'setting': setting ,
               'category': category,
               'page':'referanslar'
               }
    return render(request, 'referanslarimiz.html', context)



def iletisim(request):
    if request.method == 'POST':
        form = ContactFormu(request.POST)
        if form.is_valid():
            data= ContactFormMessage()
            data.name= form.cleaned_data['name']
            data.email = form.cleaned_data['email']
            data.subject = form.cleaned_data['subject']
            data.message = form.cleaned_data['message']
            data.ip = request.META.get('REMOTE_ADDR')
            data.save()
            messages.success(request,"Mesajınız başarı ile gönderilmiştir.Teşekkür ederiz.")
            return HttpResponseRedirect('/iletisim')

    setting = Setting.objects.get(pk=1)
    category = Category.objects.all()
    form = ContactFormu()
    context = {'setting': setting,
               'form': form,
               'category': category,
               }
    return render(request,'iletisim.html',context)


def category_cars(request, id, slug):
    category = Category.objects.all()
    categorydata = Car.objects.filter(pk=id)
    cars = Car.objects.filter(category_id=id)
    context = {
        'cars': cars,
        'category': category,
        'categorydata ': categorydata,
    }
    return render(request, 'cars.html', context)

