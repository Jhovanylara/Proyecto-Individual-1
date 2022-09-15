<img src="https://1000marcas.net/wp-content/uploads/2020/01/logo-F1-500x281.png" width="400" title="F1Logo">

## **PROYECTO INDIVIDUAL 1-Data 03**
# *Jhovany Lara Nava* 

Este proyecto individual trata de poder crear y ejecutar correctamente una API, al recibir un conjunto de datasets, de la `Fórmula 1`, contenidos en github. https://github.com/FnegreteHenry/PI01_DATA03

Se nos consiga a trabajar con el framework FastAPI para el desarrollo. Aquí dejo el enlace donde se encuentra la documentación oficial: https://fastapi.tiangolo.com/

<img src="https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png" width="250" title="FastAPILogo">

Al final se deberán crear 4 consultas que la API pueda reponder correctamente, estas son:

- Año con más carreras.
- Piloto con mayor cantidad de primeros puestos.
- Nombre del circuito más corrido.
- Piloto con mayor cantidad de puntos en total, cuyo constructor sea de nacionalidad American o British.

#
**ESQUEMA DE SOLUCIÓN**

Lo primero que hicimos, fue ingestar los datos desde github directo a un dataframe dentro de python, para lo cual utilizamos pandas, ya que podemos leer archivos en diferentes formatos; en este caso los datos venian en formato JSON y CSV. Ya sabiendo que preguntas debía responder, aprovechamos para quitar algunos campos que no ibamos a necesitar.

Una vez ingestados los datos, creamos una base de datos SQL llamada `'F1'` (desde MySQL Workbench). ¿Ahora cómo podemos ingestar nuestros dataframes en nuestra nueva base de datos `'F1'`? 

<img src="https://www.sqlalchemy.org/img/sqla_logo.png" width="250" title="SQLAlchemyLogo">

La respuesta es con `SQL Alchemy`, a través de la función `engine`; aquí dejo un enlace con la documentación: https://docs.sqlalchemy.org/en/20/orm/quickstart.html. Una vez que tenemos el código `engine` listo para hacer cargas en nuestra base, hacemos nuestra aplicación `app.py`. 

Luego creamos el archivo users.py, contenido en la carpeta routes, donde haremos las consultas SQL a nuestra base de datos `'F1'` a través de las API's con la función .get. La manera de contestar cada pregunta, fue creando una consulta consulta en específico para cada una. Ojo aquí, a pesar de tener el código listo, necesitamos hacer correr la app y entrar a la url indicada para poder obtener un resultado de las consultas.

Para poder correr la appp, lo hacemos desde la terminal, con la instrucción: `uvicorn app:app --reload`

Una vez que tenemos nuestra base de datos en SQL, abrimos nuestro scrypt `SQL Formula1.sql` (puede ser desde Workbench) y ejecutamos todo el código del srcypt. Con esto vamos a tener las tablas relacionadas y listas para poder hacer las consultas.

Por último, y gracias a FastAPI, podemos ver el resultado de nuestras consultas, entrando en nuestro navegador al host interno: http://127.0.0.1:8000/  Ahí veremos las instrucciones para poder responder a cada consulta. Quedando así:

- Año con más carreras. `/anio`
- Piloto con mayor cantidad de primeros puestos. `/piloto1`
- Nombre del circuito más corrido. `/circuito`
- Piloto con mayor cantidad de puntos en total, cuyo constructor sea de nacionalidad American o British. `/piloto2`

#
Gracias!
![HenryLogo](https://d31uz8lwfmyn8g.cloudfront.net/Assets/logo-henry-white-lg.png)# Proyecto-Individual-1
