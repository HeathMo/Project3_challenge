CREATE TABLE bigfoot (
	number INTEGER,
	title VARCHAR,
	classification VARCHAR(20),
	timestamp VARCHAR(30),
	latitude VARCHAR(30),
	longitude VARCHAR(30)
);

SELECT * FROM bigfoot;

CREATE TABLE ufos (
	summary VARCHAR,
	city VARCHAR(100),
	state VARCHAR(10),
	date_time VARCHAR(30),
	shape VARCHAR(20),
	duration VARCHAR(30),
	stats VARCHAR,
	report_link VARCHAR,
	text VARCHAR,
	posted VARCHAR(30),
	latitude VARCHAR(30),
	longitude VARCHAR(30)
);

SELECT classification, latitude, longitude
FROM bigfoot
WHERE classification = 'Class A';

/*West coast of the US*/
SELECT * FROM bigfoot
WHERE longitude BETWEEN '-115' AND '-125';

/*count response 1033*/
SELECT count(title)
FROM bigfoot
WHERE longitude BETWEEN '-115' AND '-125';

/*East coast of the US*/
SELECT * FROM bigfoot
WHERE longitude BETWEEN '-65' AND '-85';

/*count response 1190*/
SELECT count(title)
FROM bigfoot
WHERE longitude BETWEEN '-65' AND '-85';

/*Middle of the US - none generated*/
SELECT * FROM bigfoot
WHERE longitude BETWEEN '-90' AND '-110';

/*count response 0*/
SELECT count(title)
FROM bigfoot
WHERE longitude BETWEEN '-90' AND '-110';

CREATE TABLE ufo_scrubbed (
	datetime VARCHAR(40),
	city VARCHAR(100),
	state VARCHAR(10),
	shape VARCHAR(30),
	seconds VARCHAR(20),
	hours_min VARCHAR(100),
	comments VARCHAR,
	date_posted VARCHAR(20),
	latitude VARCHAR(20),
	longitude VARCHAR(20)
);

SELECT * FROM ufo_scrubbed;
