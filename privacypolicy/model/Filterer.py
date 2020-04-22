from sklearn.linear_model import LogisticRegression
import numpy as np
import pickle

class Filterer():
	
	def __init__(self):
		self.threshold = {"type1" : 0.60, "type2" : 0.50, "type3" : 0.55, "type4" : 0.50, "type5" : 0.60, "type6" : 0.50}

	def predict(self, dataset, data, Type):
		filename = "privacypolicy/model/FilteringWeightsLR/" + Type + ".sav"
		logisticRegr = pickle.load(open(filename, 'rb'))

		predictions = logisticRegr.predict(dataset)
		prob = logisticRegr.predict_proba(dataset)

		filteredArray = []
		for i in range(len(predictions)):
			if predictions[i] == 1 and prob[i][1] > self.threshold[Type]:
				filteredArray.append(data[i])

		return np.array(filteredArray)