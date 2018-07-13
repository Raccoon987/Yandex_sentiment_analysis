from sklearn.externals import joblib


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
        prediction = self.predict_text(text)
        return self.classes_dict[int(prediction[0])] + " review"   