from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader, RequestContext
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def overview(request):
    # template = loader.get_template('overview/overview.html')
    # return HttpResponse(template.render())
    return render(request, 'overview/overview.html')
