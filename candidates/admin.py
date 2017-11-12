from django.contrib import admin
from .models import *


class CandidateEducationInline(admin.TabularInline):
    model = Education
    extra = 0


class CandidateExperienceInline(admin.TabularInline):
    model = Experience
    extra = 0


class CandidateSkillsInline(admin.TabularInline):
    model = Skills
    extra = 0


class CandidatesAdmin(admin.ModelAdmin):

    inlines = [CandidateEducationInline, CandidateExperienceInline, CandidateSkillsInline]

    class Meta:
        model = Candidates

admin.site.register(Candidates, CandidatesAdmin)