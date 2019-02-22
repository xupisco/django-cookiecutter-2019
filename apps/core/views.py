# -*- coding: utf-8 -*-
import json

from django.http import Http404, HttpResponse, JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.template.loader import render_to_string
from django.utils import translation
from django.views.generic import View


class StaticView(View):
    page_title = ""
    template_name = ""

    def get(self, request):
        return render(request, self.template_name, {'page_title': self.page_title})


def set_language(request, lang_code):
    if translation.check_for_language(lang_code):
        translation.activate(lang_code)
        request.session[translation.LANGUAGE_SESSION_KEY] = lang_code

    return redirect('/')


def login(request):
    return render(request, 'login.html')


def home(request):
    return render(request, 'index.html')
