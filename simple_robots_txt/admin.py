# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from solo.admin import SingletonModelAdmin

from simple_robots_txt.models import RobotsTXT


admin.site.register(RobotsTXT, SingletonModelAdmin)
