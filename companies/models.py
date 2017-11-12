from django.db import models


class CompanyCategory(models.Model):
    name = models.CharField(max_length=64, blank=True, null=True, default=None)

    def __str__(self):
        return "%s" % self.name

    class Meta:
        verbose_name = "Company Category"
        verbose_name_plural = "Company Categories"


class Companies(models.Model):
    logo = models.ImageField(upload_to='companies_images')
    name = models.CharField(max_length=64, blank=True, null=True, default=None)
    category = models.ForeignKey(CompanyCategory, blank=True, null=True, default=None)
    tagline = models.CharField(max_length=64, blank=True, null=True, default=None)
    CEO_name = models.CharField(max_length=64, blank=True, null=True, default=None)
    description = models.TextField(blank=True, null=True, default=None)
    email = models.EmailField()
    web_site = models.URLField(max_length=64, blank=True, null=True, default=None)
    phone_number = models.CharField(max_length=64, default=None)
    location = models.CharField(max_length=64, blank=True, null=True, default=None)
    facebook_profile = models.URLField(max_length=64, blank=True, null=True, default=None)
    twitter_profile = models.URLField(max_length=64, blank=True, null=True, default=None)
    linkedin_profile = models.URLField(max_length=64, blank=True, null=True, default=None)
    google_plus_profile = models.URLField(max_length=64, blank=True, null=True, default=None)
    instagram_profile = models.URLField(max_length=64, blank=True, null=True, default=None)
    dr_profile = models.URLField(max_length=64, blank=True, null=True, default=None)
    about = models.TextField(blank=True, null=True, default=None)

    def __str__(self):
        return "%s" % self.name

    def __unicode__(self):
        return "%s" % self.name

    class Meta:
        verbose_name = "Company"
        verbose_name_plural = "Companies"


class JobType(models.Model):
    job_type = models.CharField(max_length=64, blank=True, null=True, default=None)

    def __str__(self):
        return "%s" % self.job_type

    class Meta:
        verbose_name = "Job Type"
        verbose_name_plural = "Job Types"


class Job(models.Model):
    company = models.ForeignKey(Companies, related_name='job', blank=True, null=True)
    title = models.CharField(max_length=64, blank=True, null=True, default=None)
    type = models.ForeignKey(JobType, blank=True, null=True, default=None)
    description = models.TextField(blank=True, null=True, default=None)
    requirement = models.TextField(blank=True, null=True, default=None)
    dedline = models.DateField()

    def __str__(self):
        return "%s" % self.title

    def __unicode__(self):
        return "%s" % self.title

    class Meta:
        verbose_name = "Job"
        verbose_name_plural = "Jobs"
