from django.shortcuts import render
from django.views import generic
from .models import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q


def Candidates_view(request):
    context = {}
    template_name = "candidates/index.html"
    candidate = Candidates.objects.all()

    items_count = 9
    paginator = Paginator(candidate, items_count)
    page = request.GET.get('page', 1)

    try:
        candidate_page = paginator.page(page)
    except PageNotAnInteger:
        candidate_page = paginator.page(1)
    except EmptyPage:
        candidate_page = paginator.page(paginator.num_pages)

    query = request.GET.get('q')
    if query:
        candidate_page = candidate.filter(
            Q(name__iregex=query) |
            Q(last_name__iregex=query) |
            Q(profession__iregex=query) |
            Q(about__iregex=query) |
            Q(location__iregex=query) |
            Q(resume_content__iregex=query) |
            Q(education__sckool_name__iregex=query) |
            Q(education__qualification__iregex=query) |
            Q(experience__position__iregex=query) |
            Q(skills__skill__iregex=query)
        ).distinct()

    context['candidate_page'] = candidate_page
    context['candidate'] = candidate

    return render(request, template_name, context)


class candidate_details(generic.DetailView):
    template_name = "candidates/single-candidate.html"
    model = Candidates
    context_object_name = 'candidate'
    initial = {'key': 'value'}

    def get_context_data(self, **kwargs):
        context = super(candidate_details, self).get_context_data(**kwargs)
        candidate_skills = Candidates.objects.all()

        context['candidate_skills'] = candidate_skills

        return context