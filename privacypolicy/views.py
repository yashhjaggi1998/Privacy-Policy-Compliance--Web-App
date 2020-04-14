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
			scrapperRef = WebappConfig.scrapper
			vectorizeRef = WebappConfig.vectorizer
			text = "The digit is: " + str(response(X_test)[0]) + " - " + weblink
			pageContent = scrapperRef(weblink)
			type1Data = vectorizeRef("type1", pageContent)
			type2Data = vectorizeRef("type2", pageContent)
			type3Data = vectorizeRef("type3", pageContent)
			type4Data = vectorizeRef("type4", pageContent)
			type5Data = vectorizeRef("type5", pageContent)
			type6Data = vectorizeRef("type6", pageContent)
			print(type1Data.shape, "\n", type2Data.shape, "\n", type3Data.shape, "\n", type4Data.shape, "\n", type5Data.shape, "\n", type6Data.shape, "\n", )
			return render(request, "output.html", {'weblink' : weblink, 'pageContent' : pageContent})
# returning JSON response
#return JsonResponse(response)
		

class InputView(TemplateView):
	template_name = "input.html"
	form_class = InputForm

class HomeView(TemplateView):
	template_name = "home.html"

class AboutUsView(TemplateView):
	template_name = "AboutUs.html"