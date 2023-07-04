from django.db import models
from django.contrib.auth.models import User

# Create your models here.

"""ВИДЫ СПОРТА"""
class VidSporta(models.Model):
    nazvanie_vida = models.CharField(verbose_name='Название вида спорта', max_length=255)
    opisanie = models.CharField(verbose_name='Описание вида спорта', max_length=255)
    etalon_sila = models.IntegerField(verbose_name='Эталонная сила')
    etalon_vinos = models.IntegerField(verbose_name='Эталонная выносливость')
    etalon_skorost = models.IntegerField(verbose_name='Эталонная скорость')
    etalon_gibkost = models.IntegerField(verbose_name='Эталонная гибкость')
    etalon_koord = models.IntegerField(verbose_name='Эталонная координация')

    def __str__(self):
        return self.nazvanie_vida

    class Meta:
        verbose_name = 'Вид спорта'
        verbose_name_plural = 'Виды спорта'

    def get_absolute_url(self):
        return f'/VidySporta/{self.id}'

"""РЕЗУЛЬТАТЫ"""
class Rezultaty(models.Model):
    ID_polzovatelya = models.ForeignKey(User, on_delete=models.RESTRICT, verbose_name='Пользователь')
    imya_reb = models.CharField(verbose_name='Имя ребенка', max_length=255)
    pol_reb = models.CharField(verbose_name='Пол ребенка', max_length=255)
    vozr_reb = models.IntegerField(verbose_name='Возраст ребенка')
    date_prohoj_test = models.DateTimeField(verbose_name='Дата прохождения тестирования', null=True)
    rost = models.IntegerField(verbose_name='Рост')
    ves = models.FloatField(verbose_name='Вес')
    ID_vida_sporta = models.ForeignKey(VidSporta, on_delete=models.RESTRICT, verbose_name='Вид спорта', null=True)

    def __str__(self):
        return self.imya_reb

    class Meta:
        verbose_name = 'Результат'
        verbose_name_plural = 'Результаты'

"""ЭТАЛОННЫЙ РОСТ ВЕС"""
class EtolonRostVes(models.Model):
    vozrast = models.IntegerField(verbose_name='Возраст')
    rost_malch = models.IntegerField(verbose_name='Рост мальчика')
    otklon_rost_malch = models.IntegerField(verbose_name='Отклонение в росте мальчика')
    ves_malch = models.FloatField(verbose_name='Вес мальчика')
    otklon_ves_malch = models.FloatField(verbose_name='Отклонение в весе мальчика')
    rost_devoch = models.IntegerField(verbose_name='Рост девочки')
    otklon_rost_devoch = models.IntegerField(verbose_name='Отклонение в росте девочки')
    ves_devoch = models.FloatField(verbose_name='Вес девочки')
    otklon_ves_devoch = models.FloatField(verbose_name='Отклоненипе в весе девочки')

    def __str__(self):
        return str(self.vozrast)

    class Meta:
        verbose_name = 'Эталонный рост вес'
        verbose_name_plural = 'Эталонный рост вес'

"""ХАРАКТЕРИСТИКИ"""
class Harakteristiki(models.Model):
    nazvanie_harakteristiki = models.CharField(verbose_name='Название характеристики', max_length=255)
    opisanie_harakteristiki = models.CharField(verbose_name='Описание характеристики', max_length=255)

    def __str__(self):
        return self.nazvanie_harakteristiki

    class Meta:
        verbose_name = 'Характеристика'
        verbose_name_plural = 'Характеристики'

"""ХАРАКТЕРИСТИКИ СПОРТА"""
class HarakterisSporta(models.Model):
    ID_vida_sporta = models.ForeignKey(VidSporta, on_delete=models.RESTRICT, verbose_name='Название вида спорта')
    ID_harakter = models.ForeignKey(Harakteristiki, on_delete=models.RESTRICT, verbose_name='Характеристика')

    def __str__(self):
        return self.ID_vida_sporta

    class Meta:
        verbose_name = 'Характеристика спорта'
        verbose_name_plural = 'Характеристики спорта'

"""УПРАЖНЕНИЯ"""
class Uprajneniya(models.Model):
    id_harakter = models.ForeignKey(Harakteristiki, on_delete=models.RESTRICT, verbose_name='Характеристика')
    uprajnen = models.CharField(verbose_name='Упражнение', max_length=255)
    pravila_vipolnen = models.CharField(verbose_name='Правила выполнения', max_length=255)
    vozrast = models.IntegerField(verbose_name='Возраст')
    pol = models.CharField(verbose_name='Пол', max_length=255)
    normativ_na_6 = models.FloatField(verbose_name='Норматив на 6')
    normativ_na_5 = models.FloatField(verbose_name='Норматив на 5')
    normativ_na_4 = models.FloatField(verbose_name='Норматив на 4')

    def __str__(self):
        return self.uprajnen

    class Meta:
        verbose_name = 'Упражнение'
        verbose_name_plural = 'Упражнения'

"""РЕЗУЛЬТАТЫ УПРАЖНЕНИЯ"""
class RezulUpr(models.Model):
    ID_resul = models.ForeignKey(Rezultaty, on_delete=models.RESTRICT, verbose_name='Результат', null=True)
    ID_upr = models.ForeignKey(Uprajneniya, on_delete=models.RESTRICT, verbose_name='Упражнение', null=True)
    resul_upr = models.IntegerField(verbose_name='Результат упражнения')

    def __str__(self):
        return str(self.ID_resul)

    class Meta:
        verbose_name = 'Результат упражнения'
        verbose_name_plural = 'Результаты упражнений'
