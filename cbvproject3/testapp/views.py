from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from testapp.models import Company
from django.urls import reverse_lazy
# Create your views here.
class CompanyListView(ListView):
    model = Company

class CompanyDetailView(DetailView):
    model = Company
    # default template file name:company_detail.html
    # default context_object_name:company or object
class CompanyCreateView(CreateView):
    model = Company
    fields = "__all__"
    # default template file:company_form.html
class CompanyUpdateView(UpdateView):
    model = Company
    fields = ("location","ceo")
    # default template file:company_form.html

class CompanyDeleteView(DeleteView):
    model = Company
    success_url= reverse_lazy("list")