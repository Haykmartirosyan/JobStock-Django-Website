from django.shortcuts import render
from django.views import generic
from .models import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q


def Companies_view(request):
    context = {}
    template_name = "companies/index.html"

    companies = Companies.objects.all().order_by('-id')

    items_count = 10
    paginator = Paginator(companies, items_count)
    page = request.GET.get('page', 1)

    try:
        company_page = paginator.page(page)
    except PageNotAnInteger:
        company_page = paginator.page(1)
    except EmptyPage:
        company_page = paginator.page(paginator.num_pages)

    query = request.GET.get('q')
    if query:
        company_page = companies.filter(
            Q(name__iregex=query) |
            Q(tagline__iregex=query) |
            Q(description__iregex=query) |
            Q(location__iregex=query) |
            Q(about__iregex=query) |
            Q(category__name__iregex=query)
        ).distinct()

    s = request.GET.get('s')
    if s:
        company_page = companies.filter(
            Q(location__iregex=s)
        ).distinct()

    c = request.GET.get('c')
    if c:
        company_page = companies.filter(
            Q(category__name__iregex=c)
        )

    context['companies'] = companies
    context['company_page'] = company_page

    return render(request, template_name, context)


class company_detail(generic.DetailView):
    template_name = "companies/single-company.html"
    model = Companies
    context_object_name = 'company'
    initial = {'key': 'value'}

    def get_context_data(self, **kwargs):
        context = super(company_detail, self).get_context_data(**kwargs)

        return context

