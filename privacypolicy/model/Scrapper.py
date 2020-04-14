from nltk.tokenize import sent_tokenize
import numpy as np
import requests 
from bs4 import BeautifulSoup
import re

class Scrapper:
        
    def getPage(self, URL):
        data = []
        try:
            r = requests.get(URL)
            soup = BeautifulSoup(r.content, 'lxml')
        except:
            return data
        print(soup.p.get_attribute_list('class'))
        for lines in soup.findAll(['p', 'li']):
            lines = lines.text
            lines = str((lines).encode('unicode-escape').decode('utf-8'))
            lines = re.sub(r"(\\u[0-9]{3,4}[a-z]?)|(\\n)|(\\t)|(\\xa0)", '', lines)
            for line in sent_tokenize(lines):
                data.append(line)
        data = np.array(data)
        return data