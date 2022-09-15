from fastapi import APIRouter
from config.db import engine
import pandas as pd


user=APIRouter()

@user.get("/")
def Bienvenido():
    return "Bienvenido al mundo F1, porfavor complete la url con: /anio,  /piloto1, /circuito ó /piloto2"

@user.get("/anio")
def anio_con_mas_carreras():
    R1='''SELECT DISTINCT year, count(year) as NoCarreras
    FROM races
    GROUP BY year
    ORDER BY NoCarreras DESC 
    LIMIT 1;'''

    df1=pd.read_sql(R1, engine)
    dict=df1.to_dict()

    anio=dict.get('year')
    anio=list(anio.values())[0]

    carreras=dict.get('NoCarreras')
    carreras=list(carreras.values())[0]

    return {f"El año con mas carreras fué el {anio}, con un total de {carreras} carreras."}
   
@user.get("/piloto1")
def Driver_mas_No1():
    R2='''SELECT DISTINCT d.driverRef, count(d.driverRef) as primerpuesto 
    FROM drivers d JOIN results r 
    ON (d.driverId=r.driverId) AND r.position=1
    GROUP BY d.driverRef
    ORDER BY primerpuesto DESC
    LIMIT 1;'''

    df2=pd.read_sql(R2, engine)
    dict=df2.to_dict()

    piloto=dict.get('driverRef')
    piloto=list(piloto.values())[0]

    primerpuesto=dict.get('primerpuesto')
    primerpuesto=list(primerpuesto.values())[0]


    return {f"El piloto con mas primeros puestos es {piloto}, pues ha sido campeón {primerpuesto} veces."}

@user.get("/circuito")
def circuito_mas_corrido():
    R3='''SELECT DISTINCT circuitId as Circuit, name, count(circuitId) as veces_corrido 
    FROM races  
    GROUP BY Circuit
    ORDER BY veces_corrido DESC
    LIMIT 1;'''

    df3=pd.read_sql(R3, engine)
    dict=df3.to_dict()

    circuito=dict.get('name')
    circuito=list(circuito.values())[0]

    veces=dict.get('veces_corrido')
    veces=list(veces.values())[0]

    return {f"El circuito mas corrido en la historia es el {circuito}, que ha sido corrido {veces} veces."}

@user.get("/piloto2")
def piloto_con_mas_puntos_clasif_por_constructor_AmericanBritish():
    R4='''SELECT DISTINCT driverRef AS Piloto, SUM(points) as Puntos, nationality_y as Nation
    FROM tablageneral
    WHERE (nationality_y='British' OR nationality_y='American')
    GROUP BY driverRef
    ORDER BY Puntos DESC
    LIMIT 1;'''

    df4=pd.read_sql(R4, engine)
    dict=df4.to_dict()

    puntos=dict.get('Puntos')
    puntos=list(puntos.values())[0]

    piloto=dict.get('Piloto')
    piloto=list(piloto.values())[0]

    Nation=dict.get('Nation')
    Nation=list(Nation.values())[0]

    return {f"El piloto con mayor cantidad de puntos en total ({puntos}), cuyo constructor es de nacionalidad American o British, es '{piloto}' de constructor '{Nation}'"}