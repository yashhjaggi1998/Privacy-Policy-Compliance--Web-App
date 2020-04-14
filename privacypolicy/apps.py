from django.apps import AppConfig
import html,pickle
from pathlib import Path
import os
from .Scrapper import Scrapper


#from privacypolicy.model.fast_bert.prediction import BertClassificationPredictor

class WebappConfig(AppConfig):
    #name = 'logisticRegression'
    #MODEL_PATH = Path("model")
    #BERT_PRETRAINED_PATH = Path("model/uncased_L-12_H-768_A-12/")
    #LABEL_PATH = Path("label/")
    #predictor = BertClassificationPredictor(model_path = MODEL_PATH/"multilabel-emotion-fastbert-basic.bin", pretrained_path = BERT_PRETRAINED_PATH, label_path = LABEL_PATH, multi_label=True)  
	
	loaded_model = pickle.load(open('F:/BE_Project/PrivacyPolicy/privacypolicy/model/new_model.sav', 'rb'))
	sc = Scrapper()
	predictor = loaded_model.predict
	scrapper = sc.getPage

class PrivacypolicyConfig(AppConfig):
    name = 'privacypolicy'
