from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Candidates(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=None)
    image = models.ImageField(upload_to='candidates_images')
    name = models.CharField(max_length=64, blank=True, null=True, default=None)
    last_name = models.CharField(max_length=64, blank=True, null=True, default=None)
    profession = models.CharField(max_length=64, blank=True, null=True, default=None)
    about = models.TextField(blank=True, null=True, default=None)
    email = models.EmailField()
    web_site = models.URLField(max_length=64, blank=True, null=True, default=None)
    phone_number = models.CharField(max_length=64, default=None, null=True)
    location = models.CharField(max_length=64, blank=True, null=True, default=None)
    facebook_profile = models.URLField(max_length=64, blank=True, null=True, default=None)
    twitter_profile = models.URLField(max_length=64, blank=True, null=True, default=None)
    linkedin_profile = models.URLField(max_length=64, blank=True, null=True, default=None)
    google_plus_profile = models.URLField(max_length=64, blank=True, null=True, default=None)
    instagram_profile = models.URLField(max_length=64, blank=True, null=True, default=None)
    dr_profile = models.URLField(max_length=64, blank=True, null=True, default=None)
    resume_content = models.TextField(blank=True, null=True, default=None)

    def __str__(self):
        return "%s" % self.name

    def __unicode__(self):
        return "%s" % self.name

    class Meta:
        verbose_name = "Candidate"
        verbose_name_plural = "Candidates"


class Education(models.Model):
    candidate = models.ForeignKey(Candidates, related_name='education', blank=True, null=True)
    sckool_name = models.CharField(max_length=64, blank=True, null=True, default=None)
    qualification = models.CharField(max_length=64, blank=True, null=True, default=None)
    date_from = models.DateField()
    date_to = models.DateField()

    def __str__(self):
        return "%s" % self.sckool_name

    def __unicode__(self):
        return "%s" % self.sckool_name

    class Meta:
        verbose_name = "Candidate Education"
        verbose_name_plural = "Candidates Educations"


class Experience(models.Model):
    candidate = models.ForeignKey(Candidates, related_name='experience', blank=True, null=True)
    employer = models.CharField(max_length=64, blank=True, null=True, default=None)
    position = models.CharField(max_length=64, blank=True, null=True, default=None)
    date_from = models.DateField()
    date_to = models.DateField()

    def __str__(self):
        return "%s" % self.employer

    def __unicode__(self):
        return "%s" % self.employer

    class Meta:
        verbose_name = "Candidate Experience"
        verbose_name_plural = "Candidates Experiences"


class Skills(models.Model):
    candidate = models.ForeignKey(Candidates, related_name='skills', blank=True, null=True)
    skill = models.CharField(max_length=64, blank=True, null=True, default=None)
    percent = models.IntegerField(default=1)

    def __str__(self):
        return "%s" % self.skill

    def __unicode__(self):
        return "%s" % self.skill

    class Meta:
        verbose_name = "Candidate Skill"
        verbose_name_plural = "Candidates Skills"

