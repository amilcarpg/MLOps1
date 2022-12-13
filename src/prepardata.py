import os
import pandas as pd 
import warnings
warnings.filterwarnings("ignore")
import matplotlib as plt
import matplotlib.pyplot as plt2 
import numpy as np ## Todo lo referente a trabajar con vectores y matrices
from scipy import stats ## Herramientas y algoritmos matemáticos para python
import seaborn as sns # Se basa en Matplotlib y la complementa en el tema de graficos y demás.

#%matplotlib inline

# Leemos los archivos csv
def read_file_csv(filename):
    path ='E:\DevP\MLOps1\MLOps1\data'
    df = pd.read_csv(os.path.join(path,"raw" ,filename)).set_index('coddoc')
    #df = pd.read_csv(os.path.join('../data/raw/', filename)).set_index('coddoc')
    print(filename, ' cargado correctamente')
    return df



# Exportamos la matriz de datos con las columnas seleccionadas
def data_exporting(df, features, filename):
    #dfp = df[features]
    dfp = df
    path ="E:\DevP\MLOps1\MLOps1\data\processed"
    dfp.to_csv(os.path.join(path, filename))
    #dfp.to_csv(os.path.join('../data/processed/', filename))
    print(filename, 'exportado correctamente en la carpeta processed')

# Realizamos la transformación de datos
def data_preparation(df):
    print(df.info)


    #Encodear varaibles 
    print("Paso 1. Encodear Variables Categoricas")
    columnas_categoricas = ["estciv","educacion","mora","vivienda","prestamo"]
    columnas_numericas = ["edad","balance","dia","duracion","campana","pdias","previo"]

    from sklearn.preprocessing import LabelEncoder # PasoN°01: Importo la libreria a usar
    for c in columnas_categoricas:
        print(str(c))
        le = LabelEncoder()                     #   PasoN°02: Instancio la funcion a desarrollar
        le.fit(df[str(c)])                #   PasoN°03: Ajusto la funcion
        df[str(c)]=le.transform(df[str(c)]) #   PasoN°04: Ejecuto la funcion
    print("Paso 1. OK")
    print("---")
    #Transforamcion de Variables
   
    print("Paso 2. Crear campo contactado")
    ## Debido al valor -1 para los clientes previamente no contactos se crea una columna con los valores 1 si han sido previamente contactados y 0 si no han sido previamente contactados
    df['contactado']= 1
    rows = (df['pdias'] == -1)
    df.loc[rows, 'contactado'] = 0
    #datasetoriginal['contactado'] =0
    print("Paso 2. OK")
    print("---")

    print("Paso 3. Crear campo  edad acotado")
 #Campo edad acotado
    df['edadacotado']=  df['edad']
    rows= (df['edad'] >= 65)
    df.loc[rows, 'edadacotado'] = 65
    print("Paso 3. OK")
    print("---")

    print("Paso 4. Crear campo balance acotado")
    #campo balance acotado
    df['balanceacotado']=  df['balance']
    rows= (df['balance'] >= 4000)
    df.loc[rows, 'balanceacotado'] = 4000
    rows= (df['balance'] <= -1000)
    df.loc[rows, 'balanceacotado'] = -1000
    print("Paso 4. OK")
    print("---")


#campo balance clase
    print("Paso 5. Crear campo balance clase")                  
    df['balanceclase']=  1

    rows= (df['balance'] >= -1000)
    df.loc[rows, 'balanceclase'] = 2

    rows= (df['balance'] >= -250)
    df.loc[rows, 'balanceclase'] = 3

    rows= (df['balance'] >= 0)
    df.loc[rows, 'balanceclase'] = 4

    rows= (df['balance'] >= 500)
    df.loc[rows, 'balanceclase'] = 5

    rows= (df['balance'] >= 2000)
    df.loc[rows, 'balanceclase'] = 6    

    rows= (df['balance'] >= 4000)
    df.loc[rows, 'balanceclase'] = 7

    rows= (df['balance'] >= 8000)
    df.loc[rows, 'balanceclase'] = 8

    rows= (df['balance'] >= 16000)
    df.loc[rows, 'balanceclase'] = 9
    print("Paso 5. OK")
    print("---")

 #Campo duracion acotado
    print("Paso 6. Crear Campo duracion acotadoe")                  
    df['balanceclase']=  1
    df['duracionacotado']=  df['duracion']

    rows= (df['duracion'] >= 500)

    df.loc[rows, 'duracionacotado'] = 500
    print("Paso 6. OK")
    print("---")

#Campo campana acotado
    print("Paso 7. Crear Campo duracion acotadoe")
    df['campanaacotado']=  df['campana']

    rows= (df['campana'] >= 6)

    df.loc[rows, 'campanaacotado'] = 6
    print("Paso 7. OK")
    print("---")


    return df



def main():
    # Preparación de data
    df1 = read_file_csv('AdquisicionAhorro.csv')
    tdf1 = data_preparation(df1)

    data_exporting(tdf1, '','AdquisicionAhorro.csv')
    




if __name__ == "__main__":
    main()
