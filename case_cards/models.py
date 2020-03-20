from django.db import models
from wagtail.core.fields import RichTextField


class CaseCards(models.Model):
    name = RichTextField(max_length=255)
    description = RichTextField(max_length=1000)
    case_url = models.CharField(max_length=200)

