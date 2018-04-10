from django.views.generic.base import TemplateView
from django.shortcuts import render
from django.http import HttpResponse
from .models import RestaurantLocation, OrderLocation
# Create your views here.

def home(request):
	all_location = RestaurantLocation.objects.all().values()
	ord_loc = OrderLocation.objects.all().values()
	name = "SEELAN"
	my_details = {
		'name':name,
		'status':"working as expected",
		'locations': all_location,
	}
	return render(request, "locations.html", my_details)

class RestaurantNames(TemplateView):
	"""Name of all available restaurants"""
	template_name = "Restaurant_Names.html"
	def get_context_data(self, **kwargs):
		context = super(RestaurantNames, self).get_context_data(**kwargs)
		context['Names'] = RestaurantLocation.objects.all().values()
		return context

		