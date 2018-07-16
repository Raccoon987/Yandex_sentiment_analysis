#! /usr/bin/env python
# -*- coding: utf-8 -*-

from sklearn.externals import joblib
import codecs


class MySentimentClassifier(object):
    def __init__(self):
        self.model = joblib.load("./dumped_lin_SVC_classifier.pkl")
        #self.vectorizer = joblib.load("./BigramUnprocessedVectorizer.pkl")
        self.classes_dict = {0: "negative", 1: "positive", -1: "prediction error"}
        
    def predict_text(self, text):
        try:
            lst = []
            lst.append(text)
            return self.model.predict(lst)
        except:
            print "prediction error"
            return -1   
        
    #def predict_list(self, list_of_texts):
    #    try:
    #        return self.model.predict(list_of_texts)
    #    except:
    #        print 'prediction error'
    #        return None    
        
    def get_prediction_message(self, text):
        #prediction = self.predict_text(codecs.encode(text, encoding="cp1251"))
        prediction = self.predict_text(text)
        return self.classes_dict[int(prediction[0])] + " review"   
    
    
obj = MySentimentClassifier()
print obj.get_prediction_message('Супер телефон! 1.QWERTY!!! Это самый лучший его плюс :)Очень удобная клавиатура! Даже письма писала, не то что смс. Причем есть чат. И телефон - не сенсорный!!! Как раз для тех, кто терпеть не может тыкать пальчиком в экранчик :) 2.Две симки, одна из который вставляется снаружи, что очень удобно! 3.Заряжала раз в 5-6 дней 4.Удобное и логичное меню 5.Большая память, слот для карты 6.По мне - работал быстро! Даже в интернете. 7.Падал, тонул, на него наступали, его кидали, им стучали о стену... Вообще, герой, а не телефон! За 1,5 года он пережил ооочень много (у меня малыш). И работал! До последнего несчастного случая((( Мега-падение... И то, сломался только динамик... Прекрасный телефон за эти деньги! Подумываю купить на замену точно такой же...  ')