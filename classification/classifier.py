from sklearn.neighbors import KNeighborsClassifier
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn.metrics import precision_recall_fscore_support
import variables.Variables as v
import variables.ConstantVariable as vc

def classify():
    #dataset_name="yeast.csv"#"hayes-roth.csv"
    path1 ="./Training.csv"
    path1="E:/bangla_chatbot-master/classification/Training.csv"
    #path2 ="Testing.csv"
    data1 = pd.read_csv(path1)
    data1=np.asarray(data1)
    X_train = data1[:,:data1.shape[1]-1]
    #X=X.astype(np.float)
    X_train=X_train.astype(np.int)
    y_train = data1[:,-1:]
    #y_train = np.unique(y_train, return_inverse=True)[1].tolist()



    knn = KNeighborsClassifier(n_neighbors=11)
    knn.fit(X_train, y_train)
    test=v.symptomMatrix

    #test=test.reshape(1,132)
    pridictions = knn.predict(test)
    #print(pridictions)
    v.checker["already identify disease"]=True
    #return pridictions[0]
    return vc.specialist[pridictions[0]]

#v.symptomMatrix[0,70]=1
#v.symptomMatrix[0,12]=1
#v.symptomMatrix[0,3]=1

#print(classify())
