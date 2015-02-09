# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http.response import HttpResponse

from simple_robots_txt.models import RobotsTXT


def robots_txt(request):
    return HttpResponse(
        RobotsTXT.get_solo().content, content_type="text/plain"
    )
