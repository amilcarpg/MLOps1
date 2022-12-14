import os
import pandas as pd 

#%matplotlib inline

# Leemos los archivos csv
def read_file_csv(filename):
    #path ='E:\DevP\MLOps1\MLOps1\data'
    #df = pd.read_csv(os.path.join(path,"raw" ,filename)).set_index('coddoc')
    df = pd.read_csv(os.path.join(os.path.dirname(__file__),'..','data','score', filename)).set_index('coddoc')
    print(filename, ' cargado correctamente')
    return df

def main():
    # Preparación de data
    df1 = read_file_csv('AdquisicionAhorro.csv')


if __name__ == "__main__":
    main()