from django.db import models

# Create your models here.
from django.db import models
from datetime import date

from django.urls import reverse


class Icecream(models.Model):
    """Мороженное"""
    name = models.CharField("Имя", max_length=100)
    description = models.TextField("Описание")


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Мороженное"
        verbose_name_plural = "Мороженное"


class Company(models.Model):
    """Компания"""
    title = models.CharField("Название", max_length=100)
    tagline = models.CharField("Слоган", max_length=100, default='')
    description = models.TextField("Описание")
    name = models.ManyToManyField(Icecream, verbose_name="Мороженое", related_name="name_icecream")

    draft = models.BooleanField("Черновик", default=False)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("company_detail", kwargs={"slug": self.url})

    class Meta:
        verbose_name = "Компания"
        verbose_name_plural = "Компании"