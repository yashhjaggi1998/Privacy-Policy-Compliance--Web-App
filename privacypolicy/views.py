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

	def tokenizeFun(self, filteredData):
		tokenizerRef = WebappConfig.tokenizer
		type1Padded = tokenizerRef(filteredData[0], "type1")
		type2Padded = tokenizerRef(filteredData[1], "type2")
		type3Padded = tokenizerRef(filteredData[2], "type3")
		type4Padded = tokenizerRef(filteredData[3], "type4")
		type5Padded = tokenizerRef(filteredData[4], "type5")
		type6Padded = tokenizerRef(filteredData[5], "type6")
		return [type1Padded, type2Padded, type3Padded, type4Padded, type5Padded, type6Padded]

	def gradeFun(self, paddedData):
		graderRef = WebappConfig.grader

		if len(paddedData[0]) < 10:
			if len(paddedData[0]) < 5:
				type1Grade = [0, 0, len(paddedData[0])]
			else:
				type1Grade = type1Grade = [0, len(paddedData[0]), 0]
		else:
			type1Grade = graderRef(paddedData[0], "type1")

		if len(paddedData[1]) < 10:
			if len(paddedData[1]) < 5:
				type2Grade = [0, 0, len(paddedData[1])]
			else:
				type2Grade = [0, len(paddedData[1]), 0]
		else:
			type2Grade = graderRef(paddedData[1], "type2")

		if len(paddedData[2]) < 2:
			if len(paddedData[2]) < 1:
				type3Grade = [0, 0, len(paddedData[2])]
			else:
				type3Grade = [0, len(paddedData[2]), 0]
		else:
			type3Grade = graderRef(paddedData[2], "type3")

		if len(paddedData[3]) < 10:
			if len(paddedData[3]) < 5:
				type4Grade = [0, 0, len(paddedData[3])]
			else:
				type4Grade = [0, len(paddedData[3]), 0]
		else:
			type4Grade = graderRef(paddedData[3], "type4")

		if len(paddedData[4]) < 1:
			type5Grade = [0, 0, len(paddedData[4])]
		else:
			type5Grade = graderRef(paddedData[4], "type5")

		if len(paddedData[5]) < 1:
			type6Grade = [0, 0, len(paddedData[5])]
		else:
			type6Grade = graderRef(paddedData[5], "type6")
		
		return [type1Grade, type2Grade, type3Grade, type4Grade, type5Grade, type6Grade]

	def calculateScore(self, gradedData):
		scores = []
		color = []
		low = 8.32
		mid = 4.99
		high = 1.66

		for i in range(len(gradedData)):
			sentenceNum = gradedData[i][0] + gradedData[i][1] + gradedData[i][2]
			if sentenceNum == 0:
				scores.append(0)
				color.append('#39ff14')
			else:
				catScore = low * gradedData[i][0] + mid * gradedData[i][1] + high * gradedData[i][2]
				catScore = int(catScore / sentenceNum * 10)
				scores.append(catScore)
				if catScore < 34:
					color.append('#ff1439')
				elif catScore < 67:
					color.append('#1439ff')
				else:
					color.append('#39ff14')

		return [scores, color]

	def get(self, request):
		if request.method == 'GET':
			# Fetch Link from GUI in string(weblink)
			weblink = self.request.GET.get('search')

			# Scrape Webpage using Scrapper Ref, check for errors
			pageContent = self.scraperFun(weblink)
			pageSize = len(pageContent)
			if pageSize < 10:
				# Handle Scrapping Unsuccessful here in this if block!! The below statement is temporary
				print("Scrapping Failure v.1")
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

			# Check for scrape v.2
			totalData = 0
			for i in range(0, 5):
				totalData = totalData + len(filteredData[i])
			if totalData < 6:
				print("Scrapping Failure v.2")
				return render(request, "output.html", {'pageContent' : pageSize})

			# Tokenize the filtered Data, Prepare for Grading 
			paddedData = self.tokenizeFun(filteredData)
			# print(paddedData[0].shape, "\n", paddedData[1].shape, "\n", paddedData[2].shape, "\n", paddedData[3].shape, "\n", paddedData[4].shape, "\n", paddedData[5].shape, "\n")
			print("Tokenized Successfully")

			# Grade the Data
			gradedData = self.gradeFun(paddedData)
			# print(gradedData[0], "\n", gradedData[1], "\n", gradedData[2], "\n", gradedData[3], "\n", gradedData[4], "\n", gradedData[5], "\n")
			print("Graded Successfully")

			# Calculate final scores
			finalOutput = self.calculateScore(gradedData)
			finalScores = finalOutput[0]
			finalColor = finalOutput[1]
			# print(finalScores)
			print("All Done!!!!")
			
			return render(request, "output.html", {'pageContent' : gradedData, 'lines' : pageSize, 'finalScores' : finalScores, 'finalColor' : finalColor})


class InputView(TemplateView):
	template_name = "input.html"
	form_class = InputForm

class HomeView(TemplateView):
	template_name = "home.html"

class AboutUsView(TemplateView):
	template_name = "AboutUs.html"