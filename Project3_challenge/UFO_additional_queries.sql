-- Please note that the double dash indicates a comment

-- Countries and number of sightings
SELECT DISTINCT(country), COUNT(country)
FROM ufo_sightings
GROUP BY country
ORDER BY COUNT(country) DESC;
---------------------------------------------------------------------------
-- Get the top 20 states with most sightings in the US
SELECT UPPER(state), COUNT(state)
FROM ufo_sightings
WHERE country = 'us'
GROUP BY state
ORDER BY COUNT(state) DESC
FETCH FIRST 20 ROWS ONLY;
---------------------------------------------------------------------------
-- Get the top 20 states with the most sightings not in the US
SELECT UPPER(state), COUNT(state)
FROM ufo_sightings
WHERE country != 'us'
GROUP BY state
ORDER BY COUNT(state) DESC
FETCH FIRST 20 ROWS ONLY;
---------------------------------------------------------------------------
--- Get the top 5 shapes for each country this is a very long SQL statement
SELECT *
FROM (
	SELECT UPPER(country), shape, COUNT(shape)
	FROM ufo_sightings
	WHERE country = 'us'
GROUP BY country, shape
ORDER BY COUNT(shape) DESC
FETCH FIRST 5 ROWS ONLY) usa
UNION ALL
SELECT *
FROM (
	SELECT UPPER(country), shape, COUNT(shape)
	FROM ufo_sightings
	WHERE country = 'ca'
GROUP BY country, shape
ORDER BY COUNT(shape) DESC
FETCH FIRST 5 ROWS ONLY) can
UNION ALL
SELECT *
FROM (
	SELECT UPPER(country), shape, COUNT(shape)
	FROM ufo_sightings
	WHERE country = 'gb'
GROUP BY country, shape
ORDER BY COUNT(shape) DESC
FETCH FIRST 5 ROWS ONLY) gbr
UNION ALL
SELECT *
FROM (
	SELECT UPPER(country), shape, COUNT(shape)
	FROM ufo_sightings
	WHERE country = 'au'
GROUP BY country, shape
ORDER BY COUNT(shape) DESC
FETCH FIRST 5 ROWS ONLY) aus;

-----------------------------------------------------------------------------------
-- Uses 0-to-9 decade the most widely used method for denominating decades. 
-- This query goes from 1940s to roughly mid-2014 (the latest data).
SELECT 'Decade: 1940 - 1949' AS "Decade", COUNT(*) AS "# of Sightings"
FROM ufo_sightings
WHERE TO_CHAR(datetime,'YYYY') BETWEEN '1940' AND '1949'
UNION ALL
SELECT 'Decade: 1950 - 1959' AS "Decade", COUNT(*) AS "# of Sightings"
FROM ufo_sightings
WHERE TO_CHAR(datetime,'YYYY') BETWEEN '1950' AND '1959'
UNION ALL
SELECT 'Decade: 1960 - 1969' AS "Decade", COUNT(*) AS "# of Sightings"
FROM ufo_sightings
WHERE TO_CHAR(datetime,'YYYY') BETWEEN '1960' AND '1969'
UNION ALL
SELECT 'Decade: 1970 - 1979' AS "Decade", COUNT(*) AS "# of Sightings"
FROM ufo_sightings
WHERE TO_CHAR(datetime,'YYYY') BETWEEN '1970' AND '1979'
UNION ALL
SELECT 'Decade: 1980 - 1989' AS "Decade", COUNT(*) AS "# of Sightings"
FROM ufo_sightings
WHERE TO_CHAR(datetime,'YYYY') BETWEEN '1980' AND '1989'
UNION ALL 
SELECT 'Decade: 1990 - 1999' AS "Decade", COUNT(*) AS "# of Sightings"
FROM ufo_sightings
WHERE TO_CHAR(datetime,'YYYY') BETWEEN '1990' AND '1999'
UNION ALL 
SELECT 'Decade: 2000 - 2014' AS "Decade", COUNT(*) AS "# of Sightings"
FROM ufo_sightings
WHERE TO_CHAR(datetime,'YYYY') BETWEEN '2000' AND '2014'
ORDER BY 1;
---------------------------------------------------------------------------------
-- This takes all data from 1910 - 2014 and counts the number of sightings by month.  
-- This equals the total number of records in the dataset.
SELECT '01' AS "Month", COUNT(*) AS "# of Sightings in month"
FROM ufo_sightings
WHERE TO_CHAR(datetime,'MM') = '01'
UNION ALL
SELECT '02' AS "Month", COUNT(*) AS "# of Sightings in month"
FROM ufo_sightings
WHERE TO_CHAR(datetime,'MM') = '02'
UNION ALL
SELECT '03' AS "Month", COUNT(*) AS "# of Sightings in month"
FROM ufo_sightings
WHERE TO_CHAR(datetime,'MM') = '03'
UNION ALL
SELECT '04' AS "Month", COUNT(*) AS "# of Sightings in month"
FROM ufo_sightings
WHERE TO_CHAR(datetime,'MM') = '04'
UNION ALL
SELECT '05' AS "Month", COUNT(*) AS "# of Sightings in month"
FROM ufo_sightings
WHERE TO_CHAR(datetime,'MM') = '05'
UNION ALL
SELECT '06' AS "Month", COUNT(*) AS "# of Sightings in month"
FROM ufo_sightings
WHERE TO_CHAR(datetime,'MM') = '06'
UNION ALL
SELECT '07' AS "Month", COUNT(*) AS "# of Sightings in month"
FROM ufo_sightings
WHERE TO_CHAR(datetime,'MM') = '07'
UNION ALL
SELECT '08' AS "Month", COUNT(*) AS "# of Sightings in month"
FROM ufo_sightings
WHERE TO_CHAR(datetime,'MM') = '08'
UNION ALL
SELECT '09' AS "Month", COUNT(*) AS "# of Sightings in month"
FROM ufo_sightings
WHERE TO_CHAR(datetime,'MM') = '09'
UNION ALL
SELECT '10' AS "Month", COUNT(*) AS "# of Sightings in month"
FROM ufo_sightings
WHERE TO_CHAR(datetime,'MM') = '10'
UNION ALL
SELECT '11' AS "Month", COUNT(*) AS "# of Sightings in month"
FROM ufo_sightings
WHERE TO_CHAR(datetime,'MM') = '11'
UNION ALL
SELECT '12' AS "Month", COUNT(*) AS "# of Sightings in month"
FROM ufo_sightings
WHERE TO_CHAR(datetime,'MM') = '12'
ORDER BY 1;
---------------------------------------------------------------------------------
