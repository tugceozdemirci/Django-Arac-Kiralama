from django.contrib import messages
from django.contrib.auth import logout, authenticate, login
from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from car.models import Car, Category, Images
from home.models import Setting, ContactFormu, ContactFormMessage
from home.forms import SearchForm, SignUpForm


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
    context = {'setting': setting,
               'category': category,
               'page': 'hakkimizda',
               }
    return render(request, 'hakkimizda.html', context)


def referanslar(request):
    setting = Setting.objects.get(pk=1)
    category = Category.objects.all()
    context = {'setting': setting,
               'category': category,
               'page': 'referanslar'
               }
    return render(request, 'referanslarimiz.html', context)


def iletisim(request):
    if request.method == 'POST':
        form = ContactFormu(request.POST)
        if form.is_valid():
            data = ContactFormMessage()
            data.name = form.cleaned_data['name']
            data.email = form.cleaned_data['email']
            data.subject = form.cleaned_data['subject']
            data.message = form.cleaned_data['message']
            data.ip = request.META.get('REMOTE_ADDR')
            data.save()
            messages.success(request, "Mesajınız başarı ile gönderilmiştir.Teşekkür ederiz.")
            return HttpResponseRedirect('/iletisim')

    setting = Setting.objects.get(pk=1)
    category = Category.objects.all()
    form = ContactFormu()
    context = {'setting': setting,
               'form': form,
               'category': category,
               }
    return render(request, 'iletisim.html', context)


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


def car_detail(request, id, slug):
    category = Category.objects.all()
    car = Car.objects.get(pk=id)
    images = Images.objects.filter(car_id=id)
    context = {'car': car,
               'category': category,
               'images': images,
               }
    return render(request, 'car_detail.html', context)


def car_search(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            category = Category.objects.all()
            query = form.cleaned_data['query']
            car = Car.objects.filter(title__icontains=query)
            context = {
                'cars': car,
                'category': category,
            }
            return render(request, 'car_search.html', context)

    return HttpResponseRedirect('/')


def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)

            # Redirect to a success page.
            return HttpResponseRedirect('/')
        else:
            messages.warning(request, "Login Hatalı !Kullanıcı adınızı yada şifreyi yanlış girdiniz.")
            return HttpResponseRedirect('/login')

    category = Category.objects.all()
    context = {'category': category,
               }
    return render(request, 'login.html', context)


def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = request.POST['username']
            password = request.POST['password1']
            user = authenticate(request, username=username, password=password)
            login(request, user)

            current_user = request.user
            data = UserProfile()
            data.user_id = current_user.id
            data.image = "images/users/user.png"
            data.save()
            messages.success(request, "Hoşgeldiniz...")
            return HttpResponseRedirect('/')

    form = SignUpForm()
    category = Category.objects.all()
    context = {'category': category,
               'form': form,
               }
    return render(request, 'signup.html', context)
