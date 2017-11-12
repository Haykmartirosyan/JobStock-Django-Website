from django.shortcuts import render
from django.views import generic
from companies.models import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q


def Jobs_view(request):
    context = {}
    template_name = "jobs/index.html"

    jobs = Job.objects.all().order_by('-id')
    company_categories = Companies.objects.all()
    job_type = JobType.objects.all()

    items_count = 10
    paginator = Paginator(jobs, items_count)
    page = request.GET.get('page', 1)

    try:
        job_page = paginator.page(page)
    except PageNotAnInteger:
        job_page = paginator.page(1)
    except EmptyPage:
        job_page = paginator.page(paginator.num_pages)

    query = request.GET.get('q')
    if query:
        job_page = jobs.filter(
            Q(title__iregex=query) |
            Q(type__job__title__iregex=query) |
            Q(description__iregex=query) |
            Q(requirement__iregex=query) |
            Q(company__category__name__iregex=query)
        ).distinct()

    s = request.GET.get('s')
    if s:
        job_page = jobs.filter(
            Q(company__location__iregex=s)
        ).distinct()

    c = request.GET.get('c')
    if c:
        job_page = jobs.filter(
            Q(company__category__name__iregex=c)
        ).distinct()

    t = request.GET.get('t')
    if t:
        job_page = jobs.filter(
            Q(type__job_type__iregex=t)
        ).distinct()

    context['job_page'] = job_page
    context['jobs'] = jobs
    context['company_categories'] = company_categories
    context['job_type'] = job_type

    return render(request, template_name, context)


class job_detail(generic.DetailView):
    template_name = 'jobs/single-job.html'
    model = Job
    context_object_name = 'job'
    initial = {'key': 'value'}

    def get_context_data(self, **kwargs):

        context = super(job_detail, self).get_context_data(**kwargs)

        return context