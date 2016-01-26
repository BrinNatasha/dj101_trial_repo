from django.http import HttpResponse
from django.shortcuts import render
from django.template import RequestContext, loader

from courses.models import Course


def index(request):
    # courses = Course.objects.all()
    # return render(request, 'index.html', {'courses': courses})
    courses = Course.objects.all()
    template = loader.get_template('index.html')
    context = RequestContext(request, {'courses': courses})
    return HttpResponse(template.render(context))


def contact(request):
    return render(request, 'contact.html')
