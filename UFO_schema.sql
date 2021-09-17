-- Please note the database is named UFO_Project_db

-- DROP TABLE "ufo_sightings";

CREATE TABLE "ufo_sightings" (
  --  id SERIAL,
    "datetime" VARCHAR(20),
    "city" VARCHAR(100),
    "state" VARCHAR(2),
    "country" VARCHAR(2),
    "shape" VARCHAR(20),
    "duration (seconds)" NUMERIC,
    "comments" VARCHAR(250),   
    "latitude" NUMERIC,   
    "longitude" NUMERIC(15)
 --	PRIMARY KEY(id)
);
/* Perform a few checks
SELECT * FROM ufo_sightings;

SELECT DISTINCT(country)
FROM ufo_sightings
ORDER BY 1 DESC;

-- Countries and number of sightings
SELECT DISTINCT(country), COUNT(country)
FROM ufo_sightings
GROUP BY country
ORDER BY COUNT(country) DESC;			   

-- Get the top 5 states with most sightings
SELECT UPPER(state), COUNT(state)
FROM ufo_sightings
GROUP BY state
ORDER BY COUNT(state) DESC
FETCH FIRST 5 ROWS ONLY;

-- Find some invalid dates
SELECT datetime 
FROM ufo_sightings
WHERE datetime NOT LIKE '%/%';

SELECT state, ROUND(SUM("duration (seconds)"),0)
FROM ufo_sightings
GROUP BY state
ORDER BY SUM("duration (seconds)") DESC;

-- To get the valid dates use this type of code 
SELECT datetime 
FROM ufo_sightings
WHERE datetime LIKE '%/%'
AND TO_DATE(datetime,'MM/DD/YYYY') >= '01/01/2000';

SELECT city, latitude, longitude  
FROM ufo_sightings
where city = 'new troy';
*/


