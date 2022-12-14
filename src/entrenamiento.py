import os
import pickle
import pandas as pd 
import warnings
warnings.filterwarnings("ignore")
import matplotlib as plt
import matplotlib.pyplot as plt2 
import numpy as np ## Todo lo referente a trabajar con vectores y matrices
from scipy import stats ## Herramientas y algoritmos matemáticos para python
import seaborn as sns # Se basa en Matplotlib y la complementa en el tema de graficos y demás.


# Leemos los archivos csv
def read_file_csv(filename):
    df = pd.read_csv(os.path.join(os.path.dirname(__file__),'..','data','processed', filename)).set_index('coddoc')
    print(filename, ' cargado correctamente')
    return df


def data_trainning(df):
    #se elimina el campo de codigo
    #df= df.drop('coddoc',axis=1)

    ## Si deseamos balancear, podemos hacerlo con toda la informacion?
# Creación de la data de train y la data de test
    print('Creando Xtrain y Xtest')
    print('---')
    from sklearn.model_selection import train_test_split
    X_train, X_test, y_train, y_test = train_test_split(df.drop('Adq_Ahorro', axis=1), # (X,y,%test,estratificacion)
        df['Adq_Ahorro'], 
        test_size=0.33,
        stratify=df['Adq_Ahorro'],
        random_state=100)

    print('Iniciando entrenamiento ADABOOST')
    print('---')
## ADA
    from sklearn.ensemble import AdaBoostClassifier # Paso01: Instancio
    # Parámetros :
    # base_estimator : Es el estimador base sobre la cual el ensamble es constuido.
    # n_estimators : Numero de estimadores con los cuales se construye el ensamble.
    # random_state : semilla aleatoria
    AdaBoost=AdaBoostClassifier(learning_rate=0.9, n_estimators=10000) # Paso02: Especifico
    AdaBoost.fit(X_train, y_train) # Paso03: Entrenamiento algoritmo

    # Paso N°04: Predecir con el algoritmo entrenado para validar
    y_pred_train=AdaBoost.predict(X_train) # Prediccion sobre el train
    y_pred_test= AdaBoost.predict(X_test) # Prediccion sobre el test

    print('Guardando Modelo')
    print('---')
    filenameModel = 'finalized_model.sav'
    #pickle.dump(AdaBoost, open(os.path.join('../model/', filenameModel), 'wb'))
    pickle.dump(AdaBoost, open(os.path.join(os.path.dirname(__file__),'..','model', filenameModel), 'wb'))

    print('Validando Modelo')
    print('---')
    from sklearn import metrics as metrics
    # Matriz de confusion
    print("Matriz confusion: Train")
    cm_train = metrics.confusion_matrix(y_train,y_pred_train)
    print(cm_train)

    print("Matriz confusion: Test")
    cm_test = metrics.confusion_matrix(y_test,y_pred_test)
    print(cm_test)

    # Accuracy
    print("Accuracy: Train")
    accuracy_train=metrics.accuracy_score(y_train,y_pred_train)
    print(accuracy_train)

    print("Accuracy: Test")
    accuracy_test=metrics.accuracy_score(y_test,y_pred_test)
    print(accuracy_test)

    # Precision
    print("Precision: Train")
    precision_train=metrics.precision_score(y_train,y_pred_train)
    print(precision_train)

    print("Precision: Test")
    precision_test=metrics.precision_score(y_test,y_pred_test)
    print(precision_test)

    # Recall
    print("Recall: Train")
    recall_train=metrics.recall_score(y_train,y_pred_train)
    print(recall_train)

    print("Recall: Test")
    recall_test=metrics.recall_score(y_test,y_pred_test)
    print(recall_test)








def main():
    # Preparación de data
    df1 = read_file_csv('AdquisicionAhorro.csv')
    tdf1 = data_trainning(df1)

    
    #Crear test y train
    #se elimina el campo de codigo
 



if __name__ == "__main__":
    main()