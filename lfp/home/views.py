from django.shortcuts import render

# Create your views here.
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import RequestContext, loader
from django.core.urlresolvers import reverse
from django.views import generic

# Create your views here.
class IndexView(generic.ListView):
    context_object_name = 'latest_question_list'
    template_name = 'home/index.html'
    def get_queryset(self):
    	"""Return the last five published questions."""
        return 