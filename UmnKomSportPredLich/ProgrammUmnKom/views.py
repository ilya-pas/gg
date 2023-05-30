from django.shortcuts import render, redirect
from django.template.defaulttags import register
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import Group, User
from .models import Polzovateli, VidSporta, Uprajneniya, Harakteristiki, HarakterisSporta, EtolonRostVes
from .forms import PolzovateliForm, VidSportaForm, UprajneniyaForm, HarakteristikiForm, HarakterisSportaForm, EtolonRostVesForm, myUserCreationForm, myUserChangeForm
from django.views.generic import DetailView, UpdateView, DeleteView

# Create your views here.

@register.filter(name='has_group')
def has_group(user, group_name):
    return user.groups.filter(name=group_name).exists()

def UserRegister(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            group = Group.objects.get(name='Родитель')
            user.groups.add(group)
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'ProgrammUmnKom/Register.html', {'form': form})


def Glav(request):
    return render(request, 'ProgrammUmnKom/GlavStr.html')

#### ------------ ВИДЫ СПОРТА ------------ ###

def VidySporta(request):
    vidy_sporta = VidSporta.objects.order_by('-id')
    return render(request, 'ProgrammUmnKom/VidySporta.html', {'vidy_sporta': vidy_sporta})

def VidySportaPois(request):
    query = request.GET.get('q')
    vidy_sporta = VidSporta.objects.filter(nazvanie_vida__icontains=query)
    return render(request, 'ProgrammUmnKom/VidySporta.html', {'vidy_sporta': vidy_sporta})

class VidySportaDetailView(DetailView):
    model = VidSporta
    template_name = 'ProgrammUmnKom/VidySportaDetailView.html'
    context_object_name = 'VidySporta'

class VidySportaUpdateView(UpdateView):
    model = VidSporta
    template_name = 'ProgrammUmnKom/VidySportaUpdateView.html'

    form_class = VidSportaForm

    success_url = '/VidySporta'

class VidySportDeleteView(DeleteView):
    model = VidSporta
    success_url = '/VidySporta'
    template_name = 'ProgrammUmnKom/Delete.html'

def VidySportaDob(request):
    error = ''
    if request.method == 'POST':
        form = VidSportaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('VidySporta')
        else:
            error = 'Форма была не верной'

    form = VidSportaForm()

    data = {
        'form': form,
        'error': error
    }

    return render(request, 'ProgrammUmnKom/VidySportaDob.html', data)

#### ------------ УПРАЖНЕНИЯ ------------ ###

def Uprajneniyas(request):
    upraj = Uprajneniya.objects.order_by('-id')
    return render(request, 'ProgrammUmnKom/Uprajneniya.html', {'upraj': upraj})

def UprajneniyasPois(request):
    query = request.GET.get('q')
    upraj = Uprajneniya.objects.filter(uprajnen__icontains=query)
    return render(request, 'ProgrammUmnKom/Uprajneniya.html', {'upraj': upraj})

class UprajneniyasDetailView(DetailView):
    model = Uprajneniya
    template_name = 'ProgrammUmnKom/UprajneniyasDetailView.html'
    context_object_name = 'Upr'

class UprajneniyasUpdateView(UpdateView):
    model = Uprajneniya
    template_name = 'ProgrammUmnKom/UprajneniyasUpdateView.html'

    form_class = UprajneniyaForm

    success_url = '/Uprajneniyas'

class UprajneniyasDeleteView(DeleteView):
    model = Uprajneniya
    success_url = '/Uprajneniyas'
    template_name = 'ProgrammUmnKom/Delete.html'

def UprajneniyasDob(request):
    error = ''
    if request.method == 'POST':
        form = UprajneniyaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Uprajneniyas')
        else:
            error = 'Форма была не верной'

    form = UprajneniyaForm()

    data = {
        'form': form,
        'error': error
    }

    return render(request, 'ProgrammUmnKom/UprajneniyasDob.html', data)

#### ------------ Пользователь ------------ ###

def Polzovatel(request):
    polz = User.objects.order_by('-id')
    return render(request, 'ProgrammUmnKom/Polzovatel.html', {'polz': polz})

def PolzovatelPois(request):
    query = request.GET.get('q')
    polz = User.objects.filter(username__icontains=query)
    return render(request, 'ProgrammUmnKom/Polzovatel.html', {'polz': polz})

class PolzovatelDetailView(DetailView):
    model = User
    template_name = 'ProgrammUmnKom/PolzovatelDetailView.html'
    context_object_name = 'Polz'

class PolzovatelUpdateView(UpdateView):
    model = User
    template_name = 'ProgrammUmnKom/PolzovatelUpdateView.html'

    form_class = myUserChangeForm

    success_url = '/Polzovatel'

def PolzovatelUpdateViewPassword(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('Polzovatel')
    else:
        form = PasswordChangeForm(user=request.user)

    return render(request, 'ProgrammUmnKom/PolzovatelUpdateViewPassword.html', {'form': form})

class PolzovatelDeleteView(DeleteView):
    model = User
    success_url = '/Polzovatel'
    template_name = 'ProgrammUmnKom/Delete.html'

def PolzovatelDob(request):
    error = ''
    if request.method == 'POST':
        form = myUserCreationForm(request.POST)
        q = request.POST["qq"]
        if form.is_valid():
            user = form.save()
            group = Group.objects.get(name=q)
            user.groups.add(group)
            return redirect('Polzovatel')
        else:
            error = 'Форма была не верной'

    form = myUserCreationForm()

    data = {
        'form': form,
        'error': error
    }

    return render(request, 'ProgrammUmnKom/PolzovatelDob.html', data)

#### ------------ ХАРАКТЕРИСТИКИ ------------ ###

def Hark(request):
    return render(request, 'ProgrammUmnKom/Hark.html')

def Harakteristika(request):
    harak = Harakteristiki.objects.order_by('-id')
    return render(request, 'ProgrammUmnKom/Harakteristika.html', {'harak': harak})

def HarakteristikaPois(request):
    query = request.GET.get('q')
    harak = Harakteristiki.objects.filter(nazvanie_harakteristiki__icontains=query)
    return render(request, 'ProgrammUmnKom/Harakteristika.html', {'harak': harak})

class HarakteristikaDetailView(DetailView):
    model = Harakteristiki
    template_name = 'ProgrammUmnKom/HarakteristikaDetailView.html'
    context_object_name = 'Harakter'

class HarakteristikaUpdateView(UpdateView):
    model = Harakteristiki
    template_name = 'ProgrammUmnKom/HarakteristikaUpdateView.html'

    form_class = HarakteristikiForm

    success_url = '/Hark/Harakteristika'

class HarakteristikaDeleteView(DeleteView):
    model = Harakteristiki
    success_url = '/Hark/Harakteristika'
    template_name = 'ProgrammUmnKom/Delete.html'

def HarakteristikaDob(request):
    error = ''
    if request.method == 'POST':
        form = HarakteristikiForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Harakteristika')
        else:
            error = 'Форма была не верной'

    form = HarakteristikiForm()

    data = {
        'form': form,
        'error': error
    }

    return render(request, 'ProgrammUmnKom/HarakteristikaDob.html', data)

#### ------------ ХАРАКТЕРИСТИКИ И СПОРТ ------------ ###

def HarakteristikaSport(request):
    harak_sport = HarakterisSporta.objects.order_by('-id')
    return render(request, 'ProgrammUmnKom/HarakteristikaSport.html', {'harak_sport': harak_sport})

def HarakteristikaSportPois(request):
    query = request.GET.get('q')
    sport = VidSporta.objects.order_by('-id')
    harak_sport = HarakterisSporta.objects.filter(ID_vida_sporta__icontains=query)
    return render(request, 'ProgrammUmnKom/HarakteristikaSport.html', {'harak_sport': harak_sport, 'sport': sport})

class HarakteristikaSportDetailView(DetailView):
    model = HarakterisSporta
    template_name = 'ProgrammUmnKom/HarakteristikaSportDetailView.html'
    context_object_name = 'Harakter_sport'

class HarakteristikaSportUpdateView(UpdateView):
    model = HarakterisSporta
    template_name = 'ProgrammUmnKom/HarakteristikaSportUpdateView.html'

    form_class = HarakterisSportaForm

    success_url = '/Hark/HarakteristikaSport'

class HarakteristikaSportDeleteView(DeleteView):
    model = HarakterisSporta
    success_url = '/Hark/HarakteristikaSport'
    template_name = 'ProgrammUmnKom/Delete.html'

def HarakteristikaSportDob(request):
    error = ''
    if request.method == 'POST':
        form = HarakterisSportaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('HarakteristikaSport')
        else:
            error = 'Форма была не верной'

    form = HarakterisSportaForm()

    data = {
        'form': form,
        'error': error
    }

    return render(request, 'ProgrammUmnKom/HarakteristikaSportDob.html', data)

#### ------------ "ЭТАЛОННЫЙ РОСТ ВЕС" ------------ ###

def EtoloniyRostVes(request):
    etolon = EtolonRostVes.objects.order_by('-id')
    return render(request, 'ProgrammUmnKom/EtoloniyRostVes.html', {'etolon': etolon})

def EtoloniyRostVesPois(request):
    query = request.GET.get('q')
    etolon = EtolonRostVes.objects.filter(vozrast__icontains=query)
    return render(request, 'ProgrammUmnKom/EtoloniyRostVes.html', {'etolon': etolon})

class EtoloniyRostVesDetailView(DetailView):
    model = EtolonRostVes
    template_name = 'ProgrammUmnKom/EtoloniyRostVesDetailView.html'
    context_object_name = 'Etolon'

class EtoloniyRostVesUpdateView(UpdateView):
    model = EtolonRostVes
    template_name = 'ProgrammUmnKom/EtoloniyRostVesUpdateView.html'

    form_class = EtolonRostVesForm

    success_url = '/EtoloniyRostVes'

class EtoloniyRostVesDeleteView(DeleteView):
    model = EtolonRostVes
    success_url = '/EtoloniyRostVes'
    template_name = 'ProgrammUmnKom/Delete.html'

def EtoloniyRostVesSportDob(request):
    error = ''
    if request.method == 'POST':
        form = EtolonRostVesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('EtoloniyRostVes')
        else:
            error = 'Форма была не верной'

    form = EtolonRostVesForm()

    data = {
        'form': form,
        'error': error
    }

    return render(request, 'ProgrammUmnKom/EtoloniyRostVesSportDob.html', data)