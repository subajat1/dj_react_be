# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField()
    slug = models.SlugField(unique=True, null=True)

    def __str__(self):
        return self.title
