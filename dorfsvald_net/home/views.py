from django.http import HttpResponse
from django.template import RequestContext, loader
from django.shortcuts import render


def index(request):
    template = loader.get_template('home/index.html')
    context = RequestContext(request, {})
    return HttpResponse(template.render(context))