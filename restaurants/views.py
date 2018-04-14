from django.views.generic import TemplateView, ListView
from django.shortcuts import render
from django.http import HttpResponse
from .models import RestaurantLocation, OrderLocation
from django.db.models import Q
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
		# context = super(RestaurantNames, self).get_context_data(**kwargs)
		context = {}
		context['Names'] = RestaurantLocation.objects.all().values()
		return context

class RestaurantOne(ListView):
	"""display restaurant one by one based on the url inputs"""
	template_name = "Restaurant_Names.html"
	def get_queryset(self):
		avi = self.kwargs.get("avi")
		locations = RestaurantLocation.objects.filter(Q(name__icontains= avi))
		print(locations)
		return locations

		
		