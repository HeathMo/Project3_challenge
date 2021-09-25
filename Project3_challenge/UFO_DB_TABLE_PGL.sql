-- Please note the database is named UFO_Project_db

-- DROP TABLE "ufo_sightings";

CREATE TABLE "ufo_sightings" (
    "datetime" DATE,
    "city" VARCHAR(100),
    "state" VARCHAR(2),
    "country" VARCHAR(2),
    "shape" VARCHAR(20),
    "duration (seconds)" NUMERIC,
    "comments" VARCHAR(250),   
    "latitude" NUMERIC,   
    "longitude" NUMERIC
);

/* Perform a few checks
SELECT DISTINCT(country)
FROM ufo_sightings
ORDER BY 1 DESC;
SELECT DISTINCT(state)
FROM ufo_sightings
ORDER BY 1 DESC;
-- Countries and number of sightings
SELECT DISTINCT(country), COUNT(country)
FROM ufo_sightings
GROUP BY country
ORDER BY COUNT(country) DESC;			   
-- Get the top 20 states with most sightings in the US
SELECT UPPER(state), COUNT(state)
FROM ufo_sightings
WHERE country = 'us'
GROUP BY state
ORDER BY COUNT(state) DESC
FETCH FIRST 20 ROWS ONLY;
-- Get the top 20 states with most sightings not in the US
SELECT UPPER(state), COUNT(state)
FROM ufo_sightings
WHERE country != 'us'
GROUP BY state
ORDER BY COUNT(state) DESC
FETCH FIRST 20 ROWS ONLY;
*/