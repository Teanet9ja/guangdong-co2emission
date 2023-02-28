# Importing packages

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import sessionmaker


# Define database variables in a dictionary
# Note each parameter for necesarry adjustments
DB_CONFIG = {
    "database": "co2emission",
    "username": "postgres",
    "password": "postgres",
    "host": "localhost",
    "port": "5433"}


# Create flask application
app = Flask(__name__)


# Set data base connection URI in the app configuration
username = DB_CONFIG['username']
password = DB_CONFIG['password']
host = DB_CONFIG['host']
port = DB_CONFIG['port']
database = DB_CONFIG['database']

database_uri = f"postgresql://{username}:{password}@{host}:{port}/{database}"

app.config['SQLALCHEMY_DATABASE_URI'] = database_uri


# Create object to control SQLAlchemy from the flask app
db = SQLAlchemy(app)

# Create a data model objects that matches the database tables
class co2emission(db.Model):
   table_name = "co2emission"
   table_args = {"schema": "public"}
   county_name = db.Column(db.Text)
   county_code_x= db.Column(db.Integer,primary_key=True)
   city_name=db.Column(db.Text)
   area_sqkm=db.Column(db.Float)
   Northing=db.Column(db.Float)
   Easting=db.Column(db.Float)
   co2_2008=db.Column(db.Float)
   co2_2009=db.Column(db.Float)
   co2_2010=db.Column(db.Float)
   co2_2011=db.Column(db.Float)
   co2_2012=db.Column(db.Float)
   co2_2013=db.Column(db.Float)
   co2_2014=db.Column(db.Float)
   co2_2015=db.Column(db.Float)
   co2_2016=db.Column(db.Float)
   co2_2017=db.Column(db.Float)                
   min_co2=db.Column(db.Float)         
   max_co2=db.Column(db.Float)        
   avg_co2=db.Column(db.Float)          
   total_co2=db.Column(db.Float)  


# Get all information 
@app.route('/co2emission',methods= ["GET"])
def get_emission_data():
   emissiondata=[]
   for emission in db.session.query(co2emission).all():
     del emission.__dict__['_sa_instance_state'] 
     emissiondata.append(emission.__dict__)
   return jsonify(emissiondata)

# Get info using county, code or city
@app.route('/co2emission/<m>/<n>',methods= ["GET"])
def get_emission(m,n):
    emission = ""
    if(m=="county"):
        emission = co2emission.query.filter_by(county_name=n).first()
    elif(m=="code"):
        emission = co2emission.query.filter_by(county_code_x=n).first()
    elif(m=="city"):
        emission = co2emission.query.filter_by(city_name=n).all()
        d = []
        for city in emission:
           del city.__dict__['_sa_instance_state']
           data = city.__dict__
           d.append(data)
        return jsonify(d)
    del emission.__dict__['_sa_instance_state']  
    return jsonify(emission.__dict__)

# Get info using year
@app.route('/co2emission/<year>',methods= ["GET"])
def get_co2emission(year):
    if(year=="2008"):
       year_id = co2emission.co2_2008
    elif(year=="2009"):
       year_id = co2emission.co2_2009
    elif(year=="2010"):
       year_id = co2emission.co2_2010
    elif(year=="2011"):
       year_id = co2emission.co2_2011
    elif(year=="2012"):
       year_id = co2emission.co2_2012
    elif(year=="2013"):
       year_id = co2emission.co2_2013
    elif(year=="2014"):
       year_id = co2emission.co2_2014
    elif(year=="2015"):
       year_id = co2emission.co2_2015
    elif(year=="2016"):
       year_id = co2emission.co2_2016
    elif(year=="2017"):
       year_id = co2emission.co2_2017
    result = co2emission.query.with_entities(co2emission.county_code_x,co2emission.county_name,year_id).all()
    results = [tuple(row) for row in result]
    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True)