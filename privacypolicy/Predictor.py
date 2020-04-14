#!/usr/bin/env python
# coding: utf-8

# In[1]:


from sklearn.linear_model import LogisticRegression
import pickle


# In[2]:


class Predictor():
    
    def __init__(self, TYPE):
        filename = "LogisticRegression/" + TYPE + ".sav"
        self.logisticRegr = pickle.load(open(filename, 'rb'))

    def predict(self, dataset, data):
        predictions = self.logisticRegr.predict(dataset)
        prob = self.logisticRegr.predict_proba(dataset)

        count = 0
        for i in range(len(predictions)):
            if predictions[i] == 1 and prob[i][1] > 0.50:
                print(count, " : ", prob[i], " : ", data[i])
                count += 1

