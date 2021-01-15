from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.

from django.views.generic.base import View

from .models import Company


class CompanyView(View):
    def get(self, request):
        companies = Company.objects.all()
        return render(request, "company/company_list.html", {"company_list": companies})

class CompanyDetailView(View):
    def get(self, request, pk):
        company = Company.objects.get(id=pk)
        return render(request, "company/company_detail.html", {"company": company})