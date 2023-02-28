# ETL - working example

## Objectives 

In this working example, we'll implement a simple **ETL package**. 

ETL stands for Extraction-Transform-Load, and, in practice, means the code we are about to write must:

* Extract data from one or many sources. These sources are typically databases, APIs, flat files like CSV, etc;
* Transform the original data to serve our goals;
* Load the transformed data into a database created to hold our data. 

An ETL process is, more often than not, started automatically by some sort of job scheduler. In other words, ETL processes are scheduled to run win a predefined frequency. These runs extract new data, transform and load it into the database. 

Thus, our code cannot rely on human intervention during the process, but it has to report some how in case of a fatal error.

So, a complete ETL process must:

* Perform all extraction, transformation and loading without quering the user; 
* Report the current state of the process, and in case of error;
* Be able to deal with the incomming of new data.

You can read more about ETL [here](https://en.wikipedia.org/wiki/Extract,_transform,_load).

## Data

The data used will be the CO2 emission for Guangdong Province China between 2008 - 2017, which comes in a csv file format (data.csv). 

## Questions 

1. What is the CO2 emission from each district for the years 2008 - 2017?
2. What is the average CO2 emission from each district?
3. What is the minimun, maximum and total CO2 emission for each district? 