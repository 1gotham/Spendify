from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader, RequestContext
from django.contrib.auth.decorators import login_required
from django_event_cal.functions import cal_context

@login_required(login_url='login')
def overview(request, year, month):
    context = {}

    context = cal_context(context, year, month, True)

    return render(request, 'overview/overview.html', context)