from sqlalchemy import create_engine, MetaData
import pandas as pd

import os
os.system("cls")

#Primero hacemos la ingesta de las tablas desde github con pandas, importante hacerlo desde el enlace que se obtiene dando click en "RAW"
# Aprovechamos para limpiar columnas que no vamos a necesitar 
racesurl ='https://raw.githubusercontent.com/Jhovanylara/PI01_DATA02/main/Datasets/races.csv'
races=pd.read_csv(racesurl)
races.drop(columns=['url','date', 'time', 'round'], inplace=True)
results=pd.read_json('https://raw.githubusercontent.com/Jhovanylara/PI01_DATA02/main/Datasets/results.json', lines=True)
results.drop(columns=['number', 'grid', 'positionOrder', 'laps', 'time','milliseconds', 'fastestLap', 'rank', 'fastestLapTime', 'fastestLapSpeed', 'statusId' ], inplace=True)
results_complete=pd.merge(results, races, on=['raceId'])
drivers=pd.read_json('https://raw.githubusercontent.com/Jhovanylara/PI01_DATA02/main/Datasets/drivers.json', lines=True)
drivers.drop(columns=['number','code','name', 'dob','url'], inplace=True)
results_complete=pd.merge(results_complete, drivers, on=['driverId'])
constr=pd.read_json('https://raw.githubusercontent.com/Jhovanylara/PI01_DATA02/main/Datasets/constructors.json', lines=True)
constr.drop(columns=['constructorRef','url'], inplace=True)
results_complete=pd.merge(results_complete, constr, on=['constructorId'])

#Creamos una base de datos SQL llamada 'formula1'
SQLALCHEMY_DATABASE_URL = "mysql+pymysql://root:Uwovuqo_86@localhost/F1"

#Ingestamos nuestros dataframes con engine
engine = create_engine(SQLALCHEMY_DATABASE_URL)
with engine.connect() as conn, conn.begin(): 
    races.to_sql("races", conn, if_exists='append', index=False)
    results.to_sql("results", conn, if_exists='append', index=False)
    drivers.to_sql("drivers", conn, if_exists='append', index=False)
    constr.to_sql("constr", conn, if_exists='append', index=False)
    results_complete.to_sql("tablageneral", conn, if_exists='append', index=False)


meta= MetaData()

#Luego vamos a Workbench para relacionar las tablas creadas y poder hacer las consultas o querys



