from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import RequestContext, loader
from django.core.urlresolvers import reverse
from django.views import generic
from featured.models import Feature, DetailFeature
# Create your views here.
class IndexView(generic.ListView):
    context_object_name = 'latest_question_list'
    template_name = 'featured/fplaces.html'
    def get_queryset(self):
    	"""Return the last five published questions."""
        return Feature.objects.order_by('-name')[:5]

class DetailView(generic.DetailView):
    model = DetailFeature
    template_name = 'featured/fdetail.html'