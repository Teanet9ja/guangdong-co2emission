# ETL and API Demonstration Using Gungdong Co2 Emission Data
Demonstration of an ETL and API Processes using Co2 Emission Data of Guangdong Province in China.


![----------------------------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/solar.png)

<!-- ABOUT THE PROJECT -->
<h2>1. Introduction</h2>

China aims at reaching the peak of CO2 emissions before 2030. Due to the regional development differences and industrial divisions, the CO2 emissions vary from regions. Therefore, mapping the CO2 emissions is important for better understanding the emission pattern and making decisions for cutting emissions depending on different conditions.
This project demonstrates the ETL and API processes using the Guangdong Province Co2 Emission data between the year 2008 and 2017 obtained from the Carbon Emission Accounts & Datasets (CEADs) for emerging economies web platform.





![----------------------------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/solar.png)

<!-- METHODOLOGY -->
<h2>2. Methodology</h2>

<h2>ETL</h2>
This process entails the creation of an algorithm that carries out the extraction, transformation, and Loading of the Co2 Emission data into a PostgreSQL database. The extraction of the data was carried out from a local folder after the data was downloaded in a csv fomat as there was no direct link to extract the data directly from the data platform. A transformation was carried out in order to clean the data into an acceptable format for upload into the database.

<h2>API</h2>
In the Application Programming Interface, an algorithm was developed to get / retrieve information from the database to possible external users and return them in a json format on the browser. 

* Creating an algorithm that is able to automatically select the furthest seat / seats from all occupied seats.
* Suggesting and trying to keep, while possible, one empty seat in two directions.


![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/solar.png)

<!-- DATABASE -->
<h2 id = "database">3. Database</h2>

The data of the passengers and their seat preferences are going to be input through the Python code and then stored in a table within a SQL database. In this first table, we will find information about the passengers, such as their full name, ID and booking reference.

All passengers will choose their selection preference, which can be manual or automatic. The passengers who want to manually select the seats will be able to choose those that are available, at at least one seat away from others vertical and horizontally. On the other hand, the passengers that do not select their seats will have them assigned automatically at the furthest distance possible from the occupied ones.

<p align="center">Table 1. Passenger details.</p>

<center>

| Passenger              | ID            | Booking reference | Selection preference | Seat |
| :---------------------:|:-------------:| :----------------:|:--------------------:|:----:|
| Matheus Nascimento     | g20200024     | 000001            | Manual               | A1   |
| Alba Vilanova Cortezon | m20201124     | 000002            | Manual               | E10  |
| Fábio Silva            | r2016669      | 000003            | Automatic            | NaN  |
| ...                    | ...           | ...               | ...                  | ...  |

</center>

In the same database, we will also create another table that defines the plane design and its seat map, which will be expressed as a matrix, where X corresponds to the column letters (from A to F) and Y to the row numbers. 

The letters "CO" for the attribute "Column" correspond to the corridor and therefore the seat organization is similar to the one that is found in the planes used for domestic flights, which have 6 seats per row and 1 corridor in the middle. The attribute "Seat" is a primary key of this table and a foreign key of the previous one. The attribute "Occupied" indicates if the seats are available or not. Initially, all seats are not booked (Occupied == False).

<p align="center">Table 2. Seats details.</p>

<center>

| X    | Y    | Column | Row  | Seat  | Occupied  |
| :---:| :---:| :-----:| :---:| :----:| :--------:|
| 1    | 1    | A      | 1    | A1    | False     |
| 2    | 1    | B      | 1    | B1    | False     |
| 3    | 1    | C      | 1    | C1    | False     |
| 4    | 1    | CO     | 1    | CO1   | False     |
| 5    | 1    | D      | 1    | D1    | False     |
| 6    | 1    | E      | 1    | E1    | False     |
| 7    | 1    | F      | 1    | F1    | False     |
| ...  | ...  | ...    | ...  | ...   | ...       |

</center>

There are four conditions that have to be met:

* Passengers can only have one seat assigned to them.
* A seat can be occupied by one passenger or not occupied at all.
* A seat corresponds to one and only one plane.
* A plane must have at least one seat.

![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/solar.png)

<!-- WORKFLOW -->
<h2 id = "workflow">4. Workflow</h2>

The following constraints and rules were implemented:

1. Until the capacity does not reach the limit (50%), every seat must be allocated at at least one seat away from each other. As noticed in an article in the magazine Time (2020), American airlines was leaving 50% of middle seats in economy unassigned until May 31, 2020, but said that it would use those seats if necessary.

2. If passengers make a booking for multiple people, the first constraint will not be applied and they will be able to sit together.

3. The corridor can be used as a separator for two seats, fulfilling the first constraint. The positions corresponding to the corridor in the matrix cannot be selected and only exist for the previous reason and a better visualization.

All the details about the workflow can be found in <a href = "report\Presentation.pptx">this presentation</a>. As an example, Figure 2 shows how the plane (Airbus A320 - 214 (4R-ABM/N/O)) would look like while being filled with passengers.

<p align="center"> 
  <img src = "report/img/visualization.png" alt = "Code structure" width = "15%">
</p>

<p align="center">Figure 2. Resulting visualization.</p>


![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/solar.png)

<!-- AUTHORS -->
<h2 id = "authors">5. Authors</h2>

<b>Matheus Nascimento</b><br>
Bachelor's degree in Geology at <a href ="https://ufrj.br/es/" target = "_blank">Federal University of Rio de Janeiro</a><br>
Master's degree in Geospatial Technologies at <a href ="https://www.novaims.unl.pt/" target = "_blank">NOVA University of Lisbon</a>, <a href ="https://www.uni-muenster.de/en/" target = "_blank">WWU Münster</a> and <a href ="https://www.uji.es/" target = "_blank">UJI</a><br>
</p>

<b>Fábio Silva</b><br>
Bachelor's degree in Information Systems at <a href ="https://www.novaims.unl.pt/" target = "_blank">NOVA University of Lisbon</a><br>
Master's degree in Geospatial Technologies at <a href ="https://www.novaims.unl.pt/" target = "_blank">NOVA University of Lisbon</a>, <a href ="https://www.uni-muenster.de/en/" target = "_blank">WWU Münster</a> and <a href ="https://www.uji.es/" target = "_blank">UJI</a><br>
</p>

<b>Alba Vilanova Cortezón</b><br>
Bachelor's degree in Mechanical Engineering at <a href ="https://www.udl.cat/ca/en/" target = "_blank">University of Lleida</a> and <a href ="http://eng.inha.ac.kr/" target = "_blank">Inha University</a><br>
Master's degree in Geospatial Technologies at <a href ="https://www.novaims.unl.pt/" target = "_blank">NOVA University of Lisbon</a>, <a href ="https://www.uni-muenster.de/en/" target = "_blank">WWU Münster</a> and <a href ="https://www.uji.es/" target = "_blank">UJI</a><br>
</p>
