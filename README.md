# MLOps1
modelo transformado en scripts

DESCRIPCIÓN DE CASO:
El caso es un ejemplo de una campaña de marketing de una institución bancaria.
Las campañas de marketing se basan en llamadas telefónicas. A menudo, se
requiere más de un contacto para un mismo cliente, con el fin de evaluar si el
producto (depósito a plazo del banco) será (o no) suscrito.

Objetivo
Clasificar los nuevos leads como posibles nuevos clientes

Project Organization
------------

    ├── LICENSE
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── scores         <- Results from scoring model.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering)
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── prepardata.py<- Script to prepare data
    │   │
    │   ├── entrenamiento.py       <- Script to train models
    │   │                    
    │   ├── evaluar.py    <- Script to use trained models to make predictions
    │   
    └── LICENSE            <- License
