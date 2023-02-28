SET search_path TO public;

--The co2 Emission data

DROP TABLE IF EXISTS co2emission;
CREATE TABLE co2emission (
    id serial PRIMARY KEY,
    county_code_x     integer,
    county_name       VARCHAR(50),
    city_name         VARCHAR(50),
    geometry          GEOMETRY,
    area_sqkm         REAL,
    northing          REAL,
    easting           REAL,
    co2_2008          REAL,
    co2_2009          REAL,
    co2_2010          REAL,
    co2_2011          REAL,
    co2_2012          REAL,
    co2_2013          REAL,
    co2_2014          REAL,
    co2_2015          REAL,
    co2_2016          REAL,
    co2_2017          REAL,
    min_co2           REAL,
    max_co2           REAL,
    avg_co2           REAL,
    total_co2         REAL
);