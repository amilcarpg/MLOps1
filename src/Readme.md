# Ejecución de Tests

### Paso 1: Fork del Repositorio Original

Inicie sesión en Github. Luego, vaya al enlace del proyecto original y dé click al botón "Fork". Esto copiará todo el proyecto en su usuario de Github.


### Paso 2: Descargary Levantar Entorno Avanzado de Python


docker pull jupyter/pyspark-notebook
```
docker run -it --rm -p 8888:8888 jupyter/pyspark-notebook
```


### Paso 3: Configurar git

Abra una Terminal en JupyterLab e ingrese los siguientes comandos

```
git config --global user.name "<USER>"
git config --global user.email <CORREO>
```


### Paso 4: Clonar el Proyecto desde su propio Github

```
git clone https://github.com/amilcarpg/MLOps1
```


### Paso 5: Instalar los pre-requisitos

```
cd MLOps1/

pip install -r requirements.txt
```


### Paso 6: Ejecutar las pruebas en el entorno

```
cd src

python prepardata.py

python entrenamiento.py

python evaluar.py

```


### Paso 7: Guardar los cambios en el Repo

```
git add .

git commit -m "Pruebas Finalizadas"

git push

```

Ingrese su usuario y Personal Access Token de Github. Puede revisar que los cambios se hayan guardado en el repositorio. Luego, puede finalizar JupyterLab ("File" => "Shut Down").
