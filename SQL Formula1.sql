CREATE DATABASE  IF NOT EXISTS F1;
USE F1;

select @@global.secure_file_priv;

-- Declaramos las primary key
ALTER TABLE races ADD primary key(raceId);
ALTER TABLE drivers ADD primary key(driverId);
ALTER TABLE results ADD primary key(resultId);
ALTER TABLE constr ADD primary key(constructorId);

-- Cambiamos el tipo de dato
ALTER TABLE `races` CHANGE `name` `name` VARCHAR(255);
ALTER TABLE `drivers` CHANGE `driverRef` `driverRef` VARCHAR(255);
ALTER TABLE `drivers` CHANGE `nationality` `nationality` VARCHAR(255);
ALTER TABLE `results` CHANGE `raceId` `raceId` BIGINT;
ALTER TABLE `results` CHANGE `position` `position` VARCHAR(255);
ALTER TABLE `results` CHANGE `positionText` `positionText` VARCHAR(5);
ALTER TABLE `constr` CHANGE `name` `name` VARCHAR(255);
ALTER TABLE `constr` CHANGE `nationality` `nationality` VARCHAR(255);

-- Creamos indices de las tablas determinando claves foraneas
ALTER TABLE races ADD INDEX(year);
ALTER TABLE races ADD INDEX(name);
ALTER TABLE races ADD INDEX(circuitId);
ALTER TABLE drivers ADD INDEX(driverRef);
ALTER TABLE drivers ADD INDEX(nationality);
ALTER TABLE results ADD INDEX(raceId);
ALTER TABLE results ADD INDEX(driverId);
ALTER TABLE results ADD INDEX(position);
ALTER TABLE results ADD INDEX(positionText);
ALTER TABLE results ADD INDEX(points);
ALTER TABLE constr ADD INDEX(name);
ALTER TABLE constr ADD INDEX(nationality);


-- Creamos las relaciones entre las tablas, y con ellas las restricciones
ALTER TABLE results ADD CONSTRAINT `races_fk_races` FOREIGN KEY (raceId) REFERENCES races(raceId) ON DELETE RESTRICT ON UPDATE RESTRICT;
ALTER TABLE results ADD CONSTRAINT `races_fk_drivers` FOREIGN KEY (driverId) REFERENCES drivers (driverId) ON DELETE RESTRICT ON UPDATE RESTRICT;

SELECT DISTINCT name FROM RACES;
-- Aquí hice algunas consultas para luego llevarlas dentro de mi API
/*
-- Peticion responde piloto con mas puntos cuyo constructor es de nacionalidad British o American
SELECT DISTINCT driverRef AS Piloto, SUM(points) as Puntos, nationality_y as Nation
FROM tablageneral
WHERE (nationality_y='British' OR nationality_y='American')
GROUP BY driverRef
ORDER BY Puntos DESC;

-- Peticion, responde circuito mas corrido
SELECT DISTINCT circuitId as Circuit, name, count(circuitId) as veces_corrido 
FROM races  
GROUP BY Circuit
ORDER BY veces_corrido DESC
LIMIT 1;

-- Peticion de dos tablas, responde driver con mas primeros puestos
SELECT DISTINCT d.driverRef, count(d.driverRef) as primerpuesto 
FROM drivers d JOIN results r 
ON (d.driverId=r.driverId) AND r.position=1
GROUP BY d.driverRef
ORDER BY primerpuesto DESC
LIMIT 1;
 
-- Aqui se responde el año con mas carreras
SELECT DISTINCT year, count(year) as NoCarreras
FROM races
GROUP BY year
ORDER BY NoCarreras DESC 
limit 1;

*/
