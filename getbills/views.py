from django.http import (HttpResponse, HttpResponseForbidden,
                         HttpResponseRedirect)
from django.shortcuts import get_object_or_404, render, render_to_response
from django.views.generic import FormView, DetailView, ListView
from django.core.urlresolvers import reverse
from django.utils import timezone
from forms import ApplicationForm

from django.template.context import RequestContext
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def index(request):
    # question = get_object_or_404(Question, pk=question_id)
    form = ApplicationForm()
    return render(request, 'getbills/index.html', {'form': form})
    #return HttpResponse("Hello, world. You're at the getbills index.")

def thankyou(request):
    return render(request, 'getbills/thankyou.html')

def addAplication(request):
    if request.method == 'POST':
        form = ApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('getbills:thankyou'))
    else:
        form = ApplicationForm()
    return render(request, 'getbills/index.html', {'form': form})

# Create your views here.
