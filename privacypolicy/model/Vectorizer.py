import string
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.util import ngrams
import numpy as np

class Vectorizer:
	
	def __init__(self):
		self.lemmatizer = WordNetLemmatizer()
	
	def vectorize(self, kw, dataset):
		keywords = np.load("privacypolicy/model/FilteringKeywords/" + kw + "_Keywords.npy")
		datamatrix = []
		
		for line in dataset:
			dataelement = []
			present = {}
			line = line.translate(str.maketrans('', '', string.punctuation))
			words = word_tokenize(line)
			for i in range(len(words)):
				words[i] = self.lemmatizer.lemmatize(words[i].lower())
				if words[i] not in present:
					present[words[i]] = 1
				else:
					present[words[i]] = present[words[i]] + 1

			outputs = list(ngrams(words, 2))
			for output in outputs:
				twog = str(output[0])+" "+str(output[1])
				if twog not in present:
					present[twog] = 1
				else:
					present[twog] = present[twog] + 1

			outputs = list(ngrams(words, 3))
			for output in outputs:
				twog = str(output[0])+" "+str(output[1])+" "+str(output[2])
				if twog not in present:
					present[twog] = 1
				else:
					present[twog] = present[twog] + 1

			for keys in keywords:
				if keys in present:
					dataelement.append(present[keys])
				else:
					dataelement.append(0)
			datamatrix.append(dataelement)
		return np.array(datamatrix)