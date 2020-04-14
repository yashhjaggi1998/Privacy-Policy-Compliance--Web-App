from django.shortcuts import render
from .apps import WebappConfig 

from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.views.generic import TemplateView
from .forms import InputForm

class call_model(APIView):

	def scraperFun(self, weblink):
		scrapperRef = WebappConfig.scrapper
		pageContent = scrapperRef(weblink)
		return pageContent

	def vectorizeFun(self, pageContent):
		vectorizeRef = WebappConfig.vectorizer
		type1Data = vectorizeRef("type1", pageContent)
		type2Data = vectorizeRef("type2", pageContent)
		type3Data = vectorizeRef("type3", pageContent)
		type4Data = vectorizeRef("type4", pageContent)
		type5Data = vectorizeRef("type5", pageContent)
		type6Data = vectorizeRef("type6", pageContent)
		return [type1Data, type2Data, type3Data, type4Data, type5Data, type6Data]

	def filterFun(self, pageContent, vectorizedData):
		filterRef = WebappConfig.filterer
		type1Filtered = filterRef(vectorizedData[0], pageContent, "type1")
		type2Filtered = filterRef(vectorizedData[1], pageContent, "type2")
		type3Filtered = filterRef(vectorizedData[2], pageContent, "type3")
		type4Filtered = filterRef(vectorizedData[3], pageContent, "type4")
		type5Filtered = filterRef(vectorizedData[4], pageContent, "type5")
		type6Filtered = filterRef(vectorizedData[5], pageContent, "type6")
		return [type1Filtered, type2Filtered, type3Filtered, type4Filtered, type5Filtered, type6Filtered]

	def get(self, request):
		if request.method == 'GET':
			# Fetch Link from GUI in string(weblink)
			weblink = self.request.GET.get('search')

			# Scrape Webpage using Scrapper Ref, check for errors
			pageContent = self.scraperFun(weblink)
			pageSize = len(pageContent)
			if pageSize < 10:
				# Handle Scrapping Unsuccessful here in this if block!! The below statement is temporary
				return render(request, "output.html", {'pageContent' : pageSize})
			print("Scraped Successfully")

			# Vectorize the pageContent if pipeline proceeds
			vectorizedData = self.vectorizeFun(pageContent)
			# print(vectorizedData[0].shape, "\n", vectorizedData[1].shape, "\n", vectorizedData[2].shape, "\n", vectorizedData[3].shape, "\n", vectorizedData[4].shape, "\n", vectorizedData[5].shape, "\n")
			print("Vectorized Successfully")

			# Filter the vectorized Data
			filteredData = self.filterFun(pageContent, vectorizedData)
			# print(filteredData[0].shape, "\n", filteredData[1].shape, "\n", filteredData[2].shape, "\n", filteredData[3].shape, "\n", filteredData[4].shape, "\n", filteredData[5].shape, "\n")
			print("Filtered Successfully")
			
			return render(request, "output.html", {'pageContent' : pageSize})
		

class InputView(TemplateView):
	template_name = "input.html"
	form_class = InputForm

class HomeView(TemplateView):
	template_name = "home.html"

class AboutUsView(TemplateView):
	template_name = "AboutUs.html"