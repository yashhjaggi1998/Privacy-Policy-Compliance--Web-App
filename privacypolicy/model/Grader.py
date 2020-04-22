import numpy as np
from tensorflow.keras import models

class Grader(object):
	
	def grade(self, paddedSentences, Type):
		file_name = "privacypolicy/model/GraderWeights/"+str(Type)+".hdf5"
		model = models.load_model(file_name)
		count = [0, 0, 0]
		predictions = model.predict_classes(np.array(paddedSentences))
		for element in predictions:
			count[element] = count[element] + 1
		if Type == "type6" or Type == "type4":
			count[1], count[2] = count[2], count[1]
		return count