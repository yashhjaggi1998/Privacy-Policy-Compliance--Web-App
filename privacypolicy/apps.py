from django.apps import AppConfig
import os
from .model.Scrapper import Scrapper
from .model.Vectorizer import Vectorizer
from .model.Filterer import Filterer

class WebappConfig(AppConfig):

	# Scrapper Object Instantiation
	sc = Scrapper()
	scrapper = sc.getpage

	# Vectorizer Object Instantiation
	vc = Vectorizer()
	vectorizer = vc.vectorize

	# Filterer Object Instantiation
	fm = Filterer()
	filterer = fm.predict


class PrivacypolicyConfig(AppConfig):
	name = 'privacypolicy'
