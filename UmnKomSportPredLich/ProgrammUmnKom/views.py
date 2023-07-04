from django.contrib.auth.views import PasswordChangeView
from django.shortcuts import render, redirect
from django.template.defaulttags import register
from django.contrib.auth.models import Group, User
from django.urls import reverse
from django.views.generic.edit import FormMixin

import plotly.graph_objects as go
import plotly.offline as opy

from datetime import datetime

from .models import VidSporta, Uprajneniya, Harakteristiki, HarakterisSporta, EtolonRostVes, Rezultaty, RezulUpr
from .forms import VidSportaForm, UprajneniyaForm, HarakteristikiForm, HarakterisSportaForm, EtolonRostVesForm, myUserCreationForm, myUserChangeForm, RezultatyForm, RezultatyForm1, RezulUprForm, myUserChangeForm2, myPasswordChangeForm
from django.views.generic import DetailView, UpdateView, DeleteView, CreateView

# Create your views here.

@register.filter(name='has_group')
def has_group(user, group_name):
    return user.groups.filter(name=group_name).exists()


def UserRegister(request):
    if request.method == 'POST':
        form = myUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            group = Group.objects.get(name='Родитель')
            user.groups.add(group)
            return redirect('login')
    else:
        form = myUserCreationForm()
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
    har = Harakteristiki.objects.order_by('-id')
    return render(request, 'ProgrammUmnKom/Uprajneniya.html', {'upraj': upraj, 'har': har})

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

class PolzovatelUpdateViewPassword(PasswordChangeView):
    model = User
    template_name = 'ProgrammUmnKom/PolzovatelUpdateViewPassword.html'

    form_class = myPasswordChangeForm

    success_url = '/Polzovatel'

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

#### ------------ "ТЕСТИРОВАНИЕ" ------------ ###

def Testirovanie(request):
    return render(request, 'ProgrammUmnKom/Testirovanie.html')

def Nach(request):
    error = ''
    if request.method == 'POST':
        form = RezultatyForm1(request.POST)
        if form.is_valid():
            if request.user.is_authenticated:
                nosave = form.save(commit=False)
                iduser = request.user
                nosave.ID_polzovatelya = iduser
                nosave.save()
                return redirect('Skor', pk=nosave.id)
        else:
            error = 'Форма была не верной'

    form = RezultatyForm1()

    data = {
        'form': form,
        'error': error
    }

    return render(request, 'ProgrammUmnKom/TestirovanieNachalo.html', data)

#### ------------ "ТЕСТИРОВАНИЕ(СКОРОСТЬ)" ------------ ###

class Skor(DetailView):
    model = Rezultaty
    extra_context = {'upr': Uprajneniya.objects.filter(id_harakter=1)}
    template_name = 'ProgrammUmnKom/TestirovanieSkor.html'
    context_object_name = 'rez'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        rezul = []
        rez = RezulUpr.objects.filter(ID_resul=self.kwargs.get('pk', ''))
        upraj = Uprajneniya.objects.filter(id_harakter=1)

        try:
            for el in rez:
                for il in upraj:
                    if str(el.ID_upr) == il.uprajnen:
                        rezul += [il.uprajnen]
                        break

            k = 0
            rezulK1 = ''
            rezulK2 = ''

            for el in range(len(rezul)):
                k += 1
                if k == 1:
                    rezulK1 = rezul[el]
                if k == 2:
                    rezulK2 = rezul[el]

            context['rezul'] = rezul
            context['rezulK1'] = rezulK1
            context['rezulK2'] = rezulK2
            return context

        except RezulUpr.DoesNotExist:
            context = super().get_context_data(**kwargs)
            rezul = None
            context['rezul'] = rezul
            return context

class DobSkor(FormMixin, DetailView):
    model = Uprajneniya
    template_name = 'ProgrammUmnKom/TestirovanieSkorDob.html'
    context_object_name = 'upraj'
    form_class = RezulUprForm

    def get_context_data(self, *args, **kwargs):
        context = kwargs
        page_alt = Rezultaty.objects.get(id=self.kwargs.get('pk_alt', ''))
        context['page_alt'] = page_alt
        context['form'] = RezulUprForm()
        context['upraj'] = Uprajneniya.objects.get(id=self.kwargs.get('pk', ''))
        return context


    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        updated_request = request.POST.copy()

        rez = Rezultaty.objects.get(id=self.kwargs.get('pk_alt', ''))
        upraj = Uprajneniya.objects.get(id=self.kwargs.get('pk', ''))

        if float(form['resul_upr'].value()) <= upraj.normativ_na_6:
            updated_request.update({'resul_upr': 6})
            form = RezulUprForm(updated_request)
        elif float(form['resul_upr'].value()) <= upraj.normativ_na_5:
            updated_request.update({'resul_upr': 5})
            form = RezulUprForm(updated_request)
        elif float(form['resul_upr'].value()) <= upraj.normativ_na_4:
            updated_request.update({'resul_upr': 4})
            form = RezulUprForm(updated_request)
        else:
            updated_request.update({'resul_upr': 3})
            form = RezulUprForm(updated_request)

        if form.is_valid():
            myform = form.save(commit=False)
            myform.ID_resul = Rezultaty.objects.get(id=self.kwargs.get('pk_alt', ''))
            myform.ID_upr = Uprajneniya.objects.get(id=self.kwargs.get('pk', ''))
            form.save()
            return redirect('Skor', pk=rez.id)


#### ------------ "ТЕСТИРОВАНИЕ(СИЛА)" ------------ ###

class Sila(DetailView):
    model = Rezultaty
    extra_context = {'upr': Uprajneniya.objects.filter(id_harakter=2)}
    template_name = 'ProgrammUmnKom/TestirovanieSila.html'
    context_object_name = 'rez'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        rezul = []
        rez = RezulUpr.objects.filter(ID_resul=self.kwargs.get('pk', ''))
        upraj = Uprajneniya.objects.filter(id_harakter=2)

        try:
            for el in rez:
                for il in upraj:
                    if str(el.ID_upr) == il.uprajnen:
                        rezul += [il.uprajnen]
                        break

            k = 0
            rezulK1 = ''
            rezulK2 = ''
            rezulK3 = ''

            for el in range(len(rezul)):
                k += 1
                if k == 1:
                    rezulK1 = rezul[el]
                if k == 2:
                    rezulK2 = rezul[el]
                if k == 3:
                    rezulK3 = rezul[el]

            context['rezul'] = rezul
            context['rezulK1'] = rezulK1
            context['rezulK2'] = rezulK2
            context['rezulK3'] = rezulK3
            return context

        except RezulUpr.DoesNotExist:
            context = super().get_context_data(**kwargs)
            rezul = None
            context['rezul'] = rezul
            return context

class DobSila(FormMixin, DetailView):
    model = Uprajneniya
    template_name = 'ProgrammUmnKom/TestirovanieSkorDob.html'
    context_object_name = 'upraj'
    form_class = RezulUprForm

    def get_context_data(self, *args, **kwargs):
        context = kwargs
        page_alt = Rezultaty.objects.get(id=self.kwargs.get('pk_alt', ''))
        context['page_alt'] = page_alt
        context['form'] = RezulUprForm()
        context['upraj'] = Uprajneniya.objects.get(id=self.kwargs.get('pk', ''))
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        updated_request = request.POST.copy()

        rez = Rezultaty.objects.get(id=self.kwargs.get('pk_alt', ''))
        upraj = Uprajneniya.objects.get(id=self.kwargs.get('pk', ''))

        if float(form['resul_upr'].value()) >= upraj.normativ_na_6:
            updated_request.update({'resul_upr': 6})
            form = RezulUprForm(updated_request)
        elif float(form['resul_upr'].value()) >= upraj.normativ_na_5:
            updated_request.update({'resul_upr': 5})
            form = RezulUprForm(updated_request)
        elif float(form['resul_upr'].value()) >= upraj.normativ_na_4:
            updated_request.update({'resul_upr': 4})
            form = RezulUprForm(updated_request)
        else:
            updated_request.update({'resul_upr': 3})
            form = RezulUprForm(updated_request)

        if form.is_valid():
            myform = form.save(commit=False)
            myform.ID_resul = Rezultaty.objects.get(id=self.kwargs.get('pk_alt', ''))
            myform.ID_upr = Uprajneniya.objects.get(id=self.kwargs.get('pk', ''))
            form.save()
            return redirect('Sila', pk=rez.id)

#### ------------ "ТЕСТИРОВАНИЕ(ВЫНОСЛИВОСТЬ)" ------------ ###

class Vinos(DetailView):
    model = Rezultaty
    extra_context = {'upr': Uprajneniya.objects.filter(id_harakter=3)}
    template_name = 'ProgrammUmnKom/TestirovanieVinos.html'
    context_object_name = 'rez'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        rezul = []
        rez = RezulUpr.objects.filter(ID_resul=self.kwargs.get('pk', ''))
        upraj = Uprajneniya.objects.filter(id_harakter=3)

        try:
            for el in rez:
                for il in upraj:
                    if str(el.ID_upr) == il.uprajnen:
                        rezul += [il.uprajnen]
                        break

            k = 0
            rezulK1 = ''
            rezulK2 = ''


            for el in range(len(rezul)):
                k += 1
                if k == 1:
                    rezulK1 = rezul[el]
                if k == 2:
                    rezulK2 = rezul[el]


            context['rezul'] = rezul
            context['rezulK1'] = rezulK1
            context['rezulK2'] = rezulK2

            return context

        except RezulUpr.DoesNotExist:
            context = super().get_context_data(**kwargs)
            rezul = None
            context['rezul'] = rezul
            return context

class DobVinos(FormMixin, DetailView):
    model = Uprajneniya
    template_name = 'ProgrammUmnKom/TestirovanieSkorDob.html'
    context_object_name = 'upraj'
    form_class = RezulUprForm

    def get_context_data(self, *args, **kwargs):
        context = kwargs
        page_alt = Rezultaty.objects.get(id=self.kwargs.get('pk_alt', ''))
        context['page_alt'] = page_alt
        context['form'] = RezulUprForm()
        context['upraj'] = Uprajneniya.objects.get(id=self.kwargs.get('pk', ''))
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        updated_request = request.POST.copy()

        rez = Rezultaty.objects.get(id=self.kwargs.get('pk_alt', ''))
        upraj = Uprajneniya.objects.get(id=self.kwargs.get('pk', ''))
        if upraj.uprajnen == 'Бег 1 км':
            if float(form['resul_upr'].value()) <= upraj.normativ_na_6:
                updated_request.update({'resul_upr': 6})
                form = RezulUprForm(updated_request)
            elif float(form['resul_upr'].value()) <= upraj.normativ_na_5:
                updated_request.update({'resul_upr': 5})
                form = RezulUprForm(updated_request)
            elif float(form['resul_upr'].value()) <= upraj.normativ_na_4:
                updated_request.update({'resul_upr': 4})
                form = RezulUprForm(updated_request)
            else:
                updated_request.update({'resul_upr': 3})
                form = RezulUprForm(updated_request)
        else:
            if float(form['resul_upr'].value()) >= upraj.normativ_na_6:
                updated_request.update({'resul_upr': 6})
                form = RezulUprForm(updated_request)
            elif float(form['resul_upr'].value()) >= upraj.normativ_na_5:
                updated_request.update({'resul_upr': 5})
                form = RezulUprForm(updated_request)
            elif float(form['resul_upr'].value()) >= upraj.normativ_na_4:
                updated_request.update({'resul_upr': 4})
                form = RezulUprForm(updated_request)
            else:
                updated_request.update({'resul_upr': 3})
                form = RezulUprForm(updated_request)

        if form.is_valid():
            myform = form.save(commit=False)
            myform.ID_resul = Rezultaty.objects.get(id=self.kwargs.get('pk_alt', ''))
            myform.ID_upr = Uprajneniya.objects.get(id=self.kwargs.get('pk', ''))
            form.save()
            return redirect('Vinos', pk=rez.id)

#### ------------ "ТЕСТИРОВАНИЕ(ГИБКОСТЬ)" ------------ ###

class Gibkost(DetailView):
    model = Rezultaty
    extra_context = {'upr': Uprajneniya.objects.filter(id_harakter=4)}
    template_name = 'ProgrammUmnKom/TestirovanieGibkost.html'
    context_object_name = 'rez'


    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        rezul = []
        rez = RezulUpr.objects.filter(ID_resul=self.kwargs.get('pk', ''))
        upraj = Uprajneniya.objects.filter(id_harakter=4)

        try:
            for el in rez:
                for il in upraj:
                    if str(el.ID_upr) == il.uprajnen:
                        rezul += [il.uprajnen]
                        break

            k = 0
            rezulK1 = ''


            for el in range(len(rezul)):
                k += 1
                if k == 1:
                    rezulK1 = rezul[el]


            context['rezul'] = rezul
            context['rezulK1'] = rezulK1


            return context

        except RezulUpr.DoesNotExist:
            context = super().get_context_data(**kwargs)
            rezul = None
            context['rezul'] = rezul
            return context

class DobGibkost(FormMixin, DetailView):
    model = Uprajneniya
    template_name = 'ProgrammUmnKom/TestirovanieSkorDob.html'
    context_object_name = 'upraj'
    form_class = RezulUprForm

    def get_context_data(self, *args, **kwargs):
        context = kwargs
        page_alt = Rezultaty.objects.get(id=self.kwargs.get('pk_alt', ''))
        context['page_alt'] = page_alt
        context['form'] = RezulUprForm()
        context['upraj'] = Uprajneniya.objects.get(id=self.kwargs.get('pk', ''))
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        updated_request = request.POST.copy()

        rez = Rezultaty.objects.get(id=self.kwargs.get('pk_alt', ''))
        upraj = Uprajneniya.objects.get(id=self.kwargs.get('pk', ''))

        if float(form['resul_upr'].value()) >= upraj.normativ_na_6:
            updated_request.update({'resul_upr': 6})
            form = RezulUprForm(updated_request)
        elif float(form['resul_upr'].value()) >= upraj.normativ_na_5:
            updated_request.update({'resul_upr': 5})
            form = RezulUprForm(updated_request)
        elif float(form['resul_upr'].value()) >= upraj.normativ_na_4:
            updated_request.update({'resul_upr': 4})
            form = RezulUprForm(updated_request)
        else:
            updated_request.update({'resul_upr': 3})
            form = RezulUprForm(updated_request)

        if form.is_valid():
            myform = form.save(commit=False)
            myform.ID_resul = Rezultaty.objects.get(id=self.kwargs.get('pk_alt', ''))
            myform.ID_upr = Uprajneniya.objects.get(id=self.kwargs.get('pk', ''))
            form.save()
            return redirect('Gibkost', pk=rez.id)

#### ------------ "ТЕСТИРОВАНИЕ(КОРДИНАЦИЯ)" ------------ ###

class Kordin(DetailView):
    model = Rezultaty
    extra_context = {'upr': Uprajneniya.objects.filter(id_harakter=5)}
    template_name = 'ProgrammUmnKom/TestirovanieKordin.html'
    context_object_name = 'rez'


    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        rezul = []
        rez = RezulUpr.objects.filter(ID_resul=self.kwargs.get('pk', ''))
        upraj = Uprajneniya.objects.filter(id_harakter=5)

        try:
            for el in rez:
                for il in upraj:
                    if str(el.ID_upr) == il.uprajnen:
                        rezul += [il.uprajnen]
                        break

            k = 0
            rezulK1 = ''
            rezulK2 = ''

            for el in range(len(rezul)):
                k += 1
                if k == 1:
                    rezulK1 = rezul[el]
                if k == 2:
                    rezulK2 = rezul[el]

            context['rezul'] = rezul
            context['rezulK1'] = rezulK1
            context['rezulK2'] = rezulK2

            return context

        except RezulUpr.DoesNotExist:
            context = super().get_context_data(**kwargs)
            rezul = None
            context['rezul'] = rezul
            return context

class DobKordin(FormMixin, DetailView):
    model = Uprajneniya
    template_name = 'ProgrammUmnKom/TestirovanieSkorDob.html'
    context_object_name = 'upraj'
    form_class = RezulUprForm

    def get_context_data(self, *args, **kwargs):
        context = kwargs
        page_alt = Rezultaty.objects.get(id=self.kwargs.get('pk_alt', ''))
        context['page_alt'] = page_alt
        context['form'] = RezulUprForm()
        context['upraj'] = Uprajneniya.objects.get(id=self.kwargs.get('pk', ''))
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        updated_request = request.POST.copy()

        rez = Rezultaty.objects.get(id=self.kwargs.get('pk_alt', ''))
        upraj = Uprajneniya.objects.get(id=self.kwargs.get('pk', ''))

        if float(form['resul_upr'].value()) >= upraj.normativ_na_6:
            updated_request.update({'resul_upr': 6})
            form = RezulUprForm(updated_request)
        elif float(form['resul_upr'].value()) >= upraj.normativ_na_5:
            updated_request.update({'resul_upr': 5})
            form = RezulUprForm(updated_request)
        elif float(form['resul_upr'].value()) >= upraj.normativ_na_4:
            updated_request.update({'resul_upr': 4})
            form = RezulUprForm(updated_request)
        else:
            updated_request.update({'resul_upr': 3})
            form = RezulUprForm(updated_request)

        if form.is_valid():
            myform = form.save(commit=False)
            myform.ID_resul = Rezultaty.objects.get(id=self.kwargs.get('pk_alt', ''))
            myform.ID_upr = Uprajneniya.objects.get(id=self.kwargs.get('pk', ''))
            form.save()
            return redirect('Kordin', pk=rez.id)

#### ------------ "ТЕСТИРОВАНИЕ(РЕЗУЛЬТАТ)" ------------ ###

class RzulTest(DetailView):
    model = Rezultaty
    extra_context = {
        'RezUpr': RezulUpr.objects.all()
    }
    template_name = 'ProgrammUmnKom/TestirovanieRezulTest.html'
    context_object_name = 'rez'


    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)

        RezlUp1 = []
        RezlUp2 = []
        RezlUp3 = []
        RezlUp4 = []
        RezlUp5 = []

        rezultat1 = 0
        rezultat2 = 0
        rezultat3 = 0
        rezultat4 = 0
        rezultat5 = 0

        for el in RezulUpr.objects.filter(ID_resul=self.kwargs.get('pk', '')):
            for il in Uprajneniya.objects.filter(id_harakter=1):
                if str(el.ID_upr) == il.uprajnen:
                    RezlUp1 += [el.resul_upr]
        for el in RezlUp1:
            rezultat1 += el

        for el in RezulUpr.objects.filter(ID_resul=self.kwargs.get('pk', '')):
            for il in Uprajneniya.objects.filter(id_harakter=2):
                if str(el.ID_upr) == il.uprajnen:
                    RezlUp2 += [el.resul_upr]
        for el in RezlUp2:
            rezultat2 += el

        for el in RezulUpr.objects.filter(ID_resul=self.kwargs.get('pk', '')):
            for il in Uprajneniya.objects.filter(id_harakter=3):
                if str(el.ID_upr) == il.uprajnen:
                    RezlUp3 += [el.resul_upr]
        for el in RezlUp3:
            rezultat3 += el

        for el in RezulUpr.objects.filter(ID_resul=self.kwargs.get('pk', '')):
            for il in Uprajneniya.objects.filter(id_harakter=4):
                if str(el.ID_upr) == il.uprajnen:
                    RezlUp4 += [el.resul_upr]
        for el in RezlUp4:
            rezultat4 += el

        for el in RezulUpr.objects.filter(ID_resul=self.kwargs.get('pk', '')):
            for il in Uprajneniya.objects.filter(id_harakter=5):
                if str(el.ID_upr) == il.uprajnen:
                    RezlUp5 += [el.resul_upr]
        for el in RezlUp5:
            rezultat5 += el

        context['rezultat1'] = round(rezultat1 / len(RezlUp1))
        context['rezultat2'] = round(rezultat2 / len(RezlUp2))
        context['rezultat3'] = round(rezultat3 / len(RezlUp3))
        context['rezultat4'] = round(rezultat4 / len(RezlUp4))
        context['rezultat5'] = round(rezultat5 / len(RezlUp5))

        VidSpor = VidSporta.objects.all()

        context['VidSpor'] = VidSpor

        a = []

        itog1 = round(rezultat1 / len(RezlUp1))
        itog2 = round(rezultat2 / len(RezlUp2))
        itog3 = round(rezultat3 / len(RezlUp3))
        itog4 = round(rezultat4 / len(RezlUp4))
        itog5 = round(rezultat5 / len(RezlUp5))

        for el in VidSpor:
            k = 0
            if itog1 - el.etalon_skorost == 0:
                k += 1
            elif itog1 - el.etalon_skorost == -1 or itog1 - el.etalon_skorost == 1:
                k += 1
            elif itog1 - el.etalon_skorost == -3 or itog1 - el.etalon_skorost == -2:
                k += 0

            if itog2 - el.etalon_sila == 0:
                k += 1
            elif itog2 - el.etalon_sila == -1 or itog2 - el.etalon_sila == 1:
                k += 1
            elif itog2 - el.etalon_sila == -3 or itog2 - el.etalon_sila == -2:
                k += 0

            if itog3 - el.etalon_vinos == 0:
                k += 1
            elif itog3 - el.etalon_vinos == -1 or itog3 - el.etalon_vinos == 1:
                k += 1
            elif itog3 - el.etalon_vinos == -3 or itog3 - el.etalon_vinos == -2:
                k += 0

            if itog4 - el.etalon_gibkost == 0:
                k += 1
            elif itog4 - el.etalon_gibkost == -1 or itog4 - el.etalon_gibkost == 1:
                k += 1
            elif itog4 - el.etalon_gibkost == -3 or itog4 - el.etalon_gibkost == -2:
                k += 0

            if itog5 - el.etalon_koord == 0:
                k += 1
            elif itog5 - el.etalon_koord == -1 or itog5 - el.etalon_koord == 1:
                k += 1
            elif itog5 - el.etalon_koord == -3 or itog5 - el.etalon_koord == -2:
                k += 0

            if k == 5:
                a += [el.nazvanie_vida]

        context['a'] = a

        fig = go.Figure()

        fig.add_trace(go.Barpolar(name=('Скорость'), theta=[0], r=[round(rezultat1 / len(RezlUp1))]))
        fig.add_trace(go.Barpolar(name=('Сила'), theta=[72], r=[round(rezultat2 / len(RezlUp2))]))
        fig.add_trace(go.Barpolar(name=('Выносливость'), theta=[144], r=[round(rezultat3 / len(RezlUp3))]))
        fig.add_trace(go.Barpolar(name=('Гибкость'), theta=[216], r=[round(rezultat4 / len(RezlUp4))]))
        fig.add_trace(go.Barpolar(name=('Кординация'), theta=[288], r=[round(rezultat5 / len(RezlUp5))]))

        fig.update_layout(height=400, margin=dict(l=650, r=650, b=20, t=50))

        div = opy.plot(fig, auto_open=False, output_type='div')

        context['div'] = div
        return context


class ViborSporta(UpdateView):
    model = Rezultaty
    template_name = 'ProgrammUmnKom/ViborSporta.html'
    context_object_name = 'rez'
    form_class = RezultatyForm

    def get_success_url(self):
        page_alt = Rezultaty.objects.get(id=self.kwargs.get('pk', ''))
        return reverse('RzulTest', kwargs={'pk': page_alt.id})

    def get_context_data(self, *args, **kwargs):
        context = kwargs
        page_alt = VidSporta.objects.get(id=self.kwargs.get('pk_alt', ''))
        context['page_alt'] = page_alt
        context['form1'] = RezultatyForm1
        context['upraj'] = Rezultaty.objects.get(id=self.kwargs.get('pk', ''))
        return context

    def post(self, request, *args, **kwargs):
        obj = Rezultaty.objects.get(id=self.kwargs.get('pk', ''))
        obj.ID_vida_sporta = VidSporta.objects.get(id=self.kwargs.get('pk_alt', ''))
        obj.date_prohoj_test = datetime.now()
        obj.save()
        page_alt = Rezultaty.objects.get(id=self.kwargs.get('pk', ''))
        return redirect('RzulTest', pk = page_alt.id)

#### ------------ "КАРТА" ------------ ###

class Karta(DetailView):
    model = Rezultaty
    template_name = 'ProgrammUmnKom/Karta.html'
    context_object_name = 'rez'

#### ------------ "ЛИЧНЫЙ КАБИНЕТ" ------------ ###

def LichKab(request):
    return render(request, 'ProgrammUmnKom/LichKab.html')

def Istoria(request):
    ist = Rezultaty.objects.order_by('-id')
    return render(request, 'ProgrammUmnKom/IstoriaRezul.html', {'ist': ist})

def IstoriaPois(request):
    query = request.GET.get('q')
    ist = Rezultaty.objects.filter(imya_reb__icontains=query)
    return render(request, 'ProgrammUmnKom/IstoriaRezul.html', {'ist': ist})

def IzmenLichDan(request):
    return render(request, 'ProgrammUmnKom/IzmenLichDan.html')

class IzmenLichDanUpdateView(UpdateView):
    model = User
    template_name = 'ProgrammUmnKom/IzmenLichDanUpdateView.html'

    form_class = myUserChangeForm2

    success_url = '/LichKab/IzmenLichDan'

class IzmenLichDanPasswordChangeView(PasswordChangeView):
    model = User
    template_name = 'ProgrammUmnKom/IzmenLichDanPasswordChangeView.html'

    form_class = myPasswordChangeForm

    success_url = '/LichKab/IzmenLichDan'