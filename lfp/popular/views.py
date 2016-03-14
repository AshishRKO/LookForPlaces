from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import RequestContext, loader
from django.core.urlresolvers import reverse
from django.views import generic
from popular.models import Places, DetailPlaces
# Create your views here.
class IndexView(generic.ListView):
    context_object_name = 'place_list'
    template_name = 'popular/pplaces.html'
    def get_queryset(self):
    	"""Return the last five published questions."""
        return Places.objects.order_by('-name')[:5]

class DetailView(generic.DetailView):
    model = DetailPlaces
    template_name = 'popular/detail.html'