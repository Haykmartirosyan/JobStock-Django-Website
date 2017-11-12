from django.shortcuts import render
from django.views import generic
from .models import *
from companies.models import Companies
from candidates.models import Candidates


class Home(generic.TemplateView):
    template_name = "home/index.html"

    def get_context_data(self, **kwargs):
        context = {}
        company_categories = Companies.objects.all().order_by('-id')[:9]
        candidates = Candidates.objects.all().order_by('-id')

        context['company_categories'] =company_categories
        context['candidates'] = candidates

        return context