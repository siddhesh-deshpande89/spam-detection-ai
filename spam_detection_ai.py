import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline

class SpamDetection:
    
    def __init__(self) -> None:
        pass

    def spam_algorithm(self, sentence):
        data=pd.read_csv('spam.csv')
        data.info()
        data['Spam']=data['Category'].apply(lambda x:1 if x=='spam' else 0)
        data.head(5)
        X_train,X_test,y_train,y_test = train_test_split(data.Message,data.Spam,test_size=0.25)
        clf=Pipeline([
            ('vectorizer',CountVectorizer()),
            ('nb',MultinomialNB())
        ])
        clf.fit(X_train,y_train)
        return clf.predict([sentence])


    def is_spam(self, sentence) -> bool:
        result = self.spam_algorithm(sentence)
        return True if result[0] == 1 else False