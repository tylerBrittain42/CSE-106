CREATE TABLE Weather (
    date TEXT NOT NULL,
    actual_mean_temp FLOAT NOT NULL,
    actual_min_temp FLOAT NOT NULL,
    actual_max_temp FLOAT NOT NULL,
    average_min_temp FLOAT NOT NULL,
    average_max_temp FLOAT NOT NULL,
    record_min_temp FLOAT NOT NULL,
    record_max_temp FLOAT NOT NULL,
    record_min_temp_year FLOAT NOT NULL,
    record_max_temp_year FLOAT NOT NULL,
    actual_precipitation FLOAT NOT NULL ,
    average_precipitation FLOAT NOT NULL ,
    record_precipitation FLOAT NOT NULL 
);

DROP TABLE Weather

-- Q1
SELECT date, actual_precipitation
FROM Weather
WHERE actual_precipitation = (
    SELECT MAX(actual_precipitation)
    FROM Weather
    )

-- Q2
SELECT AVG(actual_max_temp)
FROM Weather
WHERE date LIKE '2014-7%'

-- Q3
SELECT date, actual_max_temp
FROM Weather
WHERE actual_max_temp = (
    SELECT MAX(actual_max_temp)
    FROM Weather
)

-- Q4
SELECT SUM(actual_precipitation)
FROM Weather
WHERE date LIKE '2014-10%'

-- Q5
SELECT date, actual_min_temp
FROM Weather
WHERE actual_min_temp < 60 and actual_max_temp > 90

