from django.apps import AppConfig

from .model.Scrapper import Scrapper
from .model.Vectorizer import Vectorizer
from .model.Filterer import Filterer
from .model.Tokenizer import Tokenizer
from .model.Grader import Grader

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

	# Tokenizer Object Instantiation
	tk = Tokenizer()
	tokenizer = tk.tokenize

	# Grader Object Instantiation
	gd = Grader()
	grader = gd.grade


class PrivacypolicyConfig(AppConfig):
	name = 'privacypolicy'
