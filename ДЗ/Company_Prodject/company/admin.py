from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Icecream, Company


admin.site.register(Icecream)

admin.site.register(Company)