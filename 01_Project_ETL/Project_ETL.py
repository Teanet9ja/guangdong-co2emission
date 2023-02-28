# Importing modules

import os
import numpy as np
import geopandas as gpd
import pandas as pd
from sqlalchemy import create_engine
import geoalchemy2
import seaborn as sns
import matplotlib.pyplot as plt


# write Shapefile into GeoDataframe and reading file
shp_file = 'data/downloaded_shp/Guangdong.shp'
gdf =gpd.read_file(shp_file)

# writing csv data into dataframe and reading file
fp = 'data/downloaded_shp/data.csv'
df = pd.read_csv(fp)


# Cleaning and Transformation of the Shapefile Attribute Table

def process_gdf(gdf):

    # Delet columns that are not needed in the attribute and set column names to lowercase
    
    gdf = gdf.drop(gdf.columns[[1, 2, 3, 5]], axis=1)
    gdf.columns = gdf.columns.str.lower()
    gdf = gdf.rename(columns={'pac': 'county_code', 'county_nam': 'county_name'})

    #Calculate Area of Polygons in Sqkm and generate the x and y values of the polygon county centroids
   
    gdf["area_sqkm"] = round(gdf.area / 10**6, 3)
    gdf['Northing'] = round(gdf.centroid.y, 3)
    gdf['Easting'] = round(gdf.centroid.x, 3)
    
    # Clean County name  and City name columns
    def first_two_words(string):
        words = string.split()
        if len(words) == 2:
            return words[0]
        else:
            return words[0] + " " + words[1]

    #gdf['county_name'] = gdf['county_name'].apply(first_two_words)
    gdf['city_name'] = gdf['city_name'].apply(first_two_words)
    
    return gdf

cleaned_shp = process_gdf(gdf)

# Convert to WGS 84 coordinate system
cleaned_shp.to_crs(epsg=4326, inplace=True) 


# Function for csv data cleaning

def clean_csv(df):
    # deleting unwanted columns and updating column names
    df = df.drop(["县区", "城市", "City Name"], axis=1)
    df = df.rename(columns={"C2008": "CO2_2008", "C2009": "CO2_2009", "C2010": "CO2_2010",
                            "C2011": "CO2_2011", "C2012": "CO2_2012", "C2013": "CO2_2013", "C2014": "CO2_2014", "C2015": "CO2_2015", "C2016": "CO2_2016", "C2017": "CO2_2017"})

    # Calculating aggregate data
    df["Min_CO2"] = df.iloc[0:120, 3:13].min(axis=1)
    df["Max_CO2"] = df.iloc[0:120, 3:13].max(axis=1)
    df["Avg_CO2"] = df.iloc[0:120, 3:13].mean(axis=1)
    df["Total_CO2"] = df.iloc[0:120, 3:13].sum(axis=1)

    # rounding up all decimals to 3 places
    df = df.round({"CO2_2008": 3, "CO2_2009": 3, "CO2_2010": 3, "CO2_2011": 3, "CO2_2012": 3, "CO2_2012": 3, "CO2_2013": 3,
                   "CO2_2014": 3, "CO2_2015": 3, "CO2_2016": 3, "CO2_2017": 3, "Min_CO2": 3, "Max_CO2": 3, "Avg_CO2": 3, "Total_CO2": 3})

    # setting the column names to lowercase
    df.columns = df.columns.str.lower()

    return df

cleaned_csv = clean_csv(df)


# Merging both csv data with shapefile data
merged_gdf = cleaned_shp.merge(cleaned_csv, left_on='county_name', right_on='county name')

# Deleting the repeated "county name" and county code columns
merged_gdf = merged_gdf.drop(merged_gdf.columns[[7,8]], axis=1)

# Writing the GeoJSON to the output directory
merged_gdf.to_file("data/cleaned_geojson/guangdong.geojson", driver="GeoJSON")


# Connecting to Database Using the SQLAlchemy

engine = create_engine('postgresql://postgres:postgres@localhost:5433/co2emission')

# converting the GeoDataFrame to PostGIS Format
merged_gdf = gpd.read_file("data/cleaned_geojson/guangdong.geojson")
#merged_gdf = gpd.read_file("data/cleaned_shp/guangdong.shp") #FOR SHAPEFILE FILE FORMAT


merged_gdf.to_postgis(
    name="co2emission",
    con=engine,
    schema="public",
    if_exists="replace",
    index=False,
    dtype={'geometry': 'Geometry'}
)


# Creating bar charts showing emission figures by city

m_gdf_srt = merged_gdf.loc[:, ["city_name", "avg_co2"]]

m_gdf_srt = m_gdf_srt.groupby("city_name").agg({"avg_co2": "sum"}).sort_values("avg_co2", ascending=False) 
m_gdf_srt = m_gdf_srt.reset_index()

pal = sns.color_palette("Oranges_d", len(m_gdf_srt))

sns.barplot(data=m_gdf_srt, x="avg_co2", y='city_name', palette=np.array(pal[::-1]), errorbar=None)

sns.set(rc={"figure.figsize":(10,6)})
sns.set(font_scale=1)
sns.set(style="whitegrid",color_codes=True)

pal = sns.color_palette("Greens_d", len(m_gdf_srt))
plt.title("Average CO2 Emission by Cities in Guangdong China")
plt.xlabel("CO2 Emission in million metric tonn")
plt.ylabel("Cities")


