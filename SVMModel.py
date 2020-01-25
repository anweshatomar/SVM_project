import datetime
import math

import arrow
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib import style
from sklearn import preprocessing, svm
from sklearn.model_selection import train_test_split

class SVMModel(object):

    def input(self,stck):

        self.stock = pd.read_csv(stck)
        self.stock.head()
        self.stock = self.stock[['Date', 'Open Price', 'High Price', 'Low Price', 'Close Price', 'Total Turnover (Rs.)']]
        self.stock.head()
        self.stock['HIGHLOW_PCT'] = (self.stock['High Price'] - self.stock['Close Price']) / (self.stock['Close Price']) * 100
        # Calculating new and old prices
        self.stock['PCT_Change'] = (self.stock['Close Price'] - self.stock['Open Price']) / (self.stock['Open Price']) * 100
        # Extracting required data from file
        self.stock = self.stock[['Close Price', 'HIGHLOW_PCT', 'PCT_Change', 'Total Turnover (Rs.)']]



    def train_test(self):
        forecast_col='Close Price'
        self.stock.fillna(-99999,inplace=True)
        self.forecast_out=int(math.ceil(0.02*len(self.stock)))
    
        self.stock['label']=self.stock[forecast_col].shift(-self.forecast_out)


        X = np.array(self.stock.drop(['label'],1))
        X = preprocessing.scale(X)
        X = X[:-self.forecast_out]
        self.X_lately=X[-self.forecast_out:]


        self.stock.dropna(inplace=True)
        y=np.array(self.stock['label'])

        self.X_train,self.X_test,self.y_train,self.y_test=train_test_split(X,y,test_size=0.5)
        
        
    def SVM(self):
        clf = svm.SVR(kernel="linear")
        clf.fit(self.X_train, self.y_train)
        accuracy = clf.score(self.X_test, self.y_test)
        print("ACCURACY OF PREDICTION:")
        print(accuracy)

        print("PREDICTION FOR THE NEXT FEW DAYS:")
        self.forecast_set = clf.predict(self.X_lately)
        print(self.forecast_set, accuracy, self.forecast_out)




    def displayGraph(self):
        style.use('ggplot')

        self.stock['Forecast'] = np.nan
        last_date = self.stock.iloc[-1].name
        last_unix = arrow.get(last_date).timestamp
        one_day = 86400
        next_unix = last_unix + one_day

        for i in self.forecast_set:
            next_date = datetime.datetime.fromtimestamp(next_unix)
            next_unix += one_day
            self.stock.loc[next_date] = [np.nan for _ in range(len(self.stock.columns) - 1)] + [i]
        print("GRAPH PLOTTED USING PREDICTED VALUES:")
        self.stock.head()
        self.stock['Close Price'].plot()
        self.stock['Forecast'].plot()
        plt.legend(loc=4)
        plt.xlabel('Date')
        plt.ylabel('Price')
        plt.show()

if __name__=="__main__":

    o=SVMModel()
    o.input("stck")
    o.train_test()
    o.SVM()
    o.displayGraph()
