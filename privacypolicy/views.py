from django.shortcuts import render
from .apps import WebappConfig 

from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .apps import WebappConfig
from django.views.generic import TemplateView

from sklearn import datasets, linear_model, metrics 
from sklearn.model_selection import train_test_split
from .forms import InputForm

class call_model(APIView):
	def get(self,request):
		if request.method == 'GET':

			weblink = self.request.GET.get('search')

			params = request.GET.get('sentence')
			digits = datasets.load_digits() 
			X = digits.data 
			y = digits.target

			X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4,random_state=1) 
			
			response = WebappConfig.predictor
			text = "The digit is: " + str(response(X_test)[0]) + " - " + weblink
			return render(request, "output.html", {'weblink' : weblink, })
# returning JSON response
#return JsonResponse(response)
		

class InputView(TemplateView):
	template_name = "input.html"
	form_class = InputForm

class HomeView(TemplateView):
	template_name = "home.html"

class AboutUsView(TemplateView):
	template_name = "AboutUs.html"