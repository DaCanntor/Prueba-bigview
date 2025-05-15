# Prueba Big View
## Para inicializar el FastApi
### Pasos a proseguir:
#### Descargar Ultima Version de Python 3.x
#### Instalar el entorno (Windows) virtual con el siguiente comando `python -m venv env` para luego activarlo con el comando `.\env\Scripts\activate` (opcional, pero recomendado)
###### Instalar el entorno (Linux) virtual con el siguiente comando `python3 -m venv env` para luego activarlo con el comando `source env/bin/activate` (opcional, pero recomendado)
#### Luego instala los componente requeridos usando el siguiente comando `pip install -r requirements.txt` cuyos requerimientos se encuentran anexados al archivo de texto dentro del proyecto
#### Se ejecutara el servidor con el comando `uvicorn main:app --reload`
#### y esta sera la URL para el ingreso del proyecto (http://127.0.0.1:8000/docs)
#### Para cerrar el entorno ejecuta el sigueinte comando `deactivate`
##### Este proyecto es una API de usuarios simple construida con FastAPI. Permite consultar y crear usuarios mediante los endpoints:

- `GET /users/{user_id}`
- `POST /users/`

## Para inicializar las pruebas del archivo "test_app.py"
### Se tiene que ejecutar el siguiente comando `pytest test_main.py`

### Para poder ejecutar las pruebas automaticas del archivo "test_selenium.py" encontrado en la carpeta "test_selenium" se debe ejecutar los siguientes pasos:
- Descargar los siguientes archivos Chrome `https://storage.googleapis.com/chrome-for-testing-public/138.0.7179.0/win64/chromedriver-win64.zip` y `https://storage.googleapis.com/chrome-for-testing-public/138.0.7179.0/win64/chrome-win64.zip`
- adicional extraer estos archivos y crear una carpeta en el disco local `C:/` y nombrarla `WebDriver`
- y coloca las carpetas extraidas de los archivos Chrome dentro de la carpeta `WebDriver`
- Instalar selenium mediante el siguiente comando `pip install selenium`
- ejecutar el comando `python test_selenium/test_selenium.py` para colocar en marcha la prueba
- (Dato adicional: al momento de generar el proceso y finzalizado este mismo generara un archivo llamado `video.json` que contendra los datos requeridos)

## 📚 Librerías utilizadas
- FastAPI: para construir la API.

- Uvicorn: servidor ASGI para correr FastAPI.

- Pytest: para realizar pruebas unitarias.

- httpx / TestClient: cliente para simular peticiones HTTP a la API.

- Selenium

- YoutubeDL
