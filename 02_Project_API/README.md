# REST API Working example

The code here demonstrates how to create a REST API using Flask.
It allows for connection to the PostgreSQL database and creates GET endpoints that allows user to Read  data in the database.

## What is flask?

Flask is a web framework, it’s a Python module that lets you develop web applications easily.

## Requisites

This code makes use of the CO2 emission data for Guangdung China from 2008 - 2017. A database is created and populated using the ETL pipeline from the Project_ETL code

## How to run it?

1. Make sure to install the packages in requirements.txt on your environment
2. Run the `create_db.sql` file
3. Start the application running:

   ```
   python main.py
   ```
4. The application will start and will be available on `localhost:5000`

# How to test it

1. Install Postman from `https://www.postman.com/downloads/`
2. Open postman and try to do some requests
3. Try a GET with `localhost:5000/co2emission` to get all the data available for all districts or county
4. Try a GET with `localhost:5000/co2emission/city` to get the data available for one city
5. Try a GET with `localhost:5000/co2emission/code` to get the data available for a district or county 
6. Try a GET with `localhost:5000/co2emission/county` to get the data available for a district or county 
7. Try a GET with `localhost:5000/co2emission/year` to get the co2 emission of all districts for a year

