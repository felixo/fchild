from django.http import (HttpResponse, HttpResponseForbidden,
                         HttpResponseRedirect)
from django.shortcuts import get_object_or_404, render, render_to_response
from django.views.generic import FormView, DetailView, ListView
from django.core.urlresolvers import reverse
from django.utils import timezone


from django.template.context import RequestContext
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def index(request):
    # question = get_object_or_404(Question, pk=question_id)
    # form = ArtForm()
    return render(request, 'getbills/index.html')
    #return HttpResponse("Hello, world. You're at the getbills index.")


# Create your views here.
