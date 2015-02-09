# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from solo.models import SingletonModel


@python_2_unicode_compatible
class RobotsTXT(SingletonModel):
    content = models.TextField()

    class Meta:
        verbose_name = 'robots.txt'

    def __str__(self):
        return 'robots.txt'
