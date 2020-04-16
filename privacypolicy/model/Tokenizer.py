import numpy as np
import pickle
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences

class Tokenizer:

	def __init__(self):
		self.max_len = {"type1" : 50, "type2" : 30, "type3" : 40, "type4" : 50, "type5" : 30, "type6" : 40}
		self.trunc_type='post'
		self.padding_type='post'

	def tokenize(self, sentences, Type):
		file_name = "privacypolicy/model/Tokenizers/token_"+str(Type)+".pickle"
		with open(file_name, 'rb') as handle:
			tokenizer = pickle.load(handle)

		# Tokenize and Pad the sentences
		sequences = tokenizer.texts_to_sequences(sentences)
		padded = pad_sequences(sequences, maxlen=self.max_len[Type], padding=self.padding_type, truncating=self.trunc_type)
		return padded