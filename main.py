import requests
import pandas as pd
import pyarrow
import sqlite3

#--Defining URL --
url = "https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2025-01.parquet"

response = requests.get(url, stream=True)

if response.status_code == 200:
    print("File downloaded successfully.")
    
    #-- Saving the file as 25.01.parquet --
    with open("25.01.parquet", "wb") as file:
        for chunk in response.iter_content(chunk_size=8192):
            if chunk:
                file.write(chunk)
    print("File saved as 25.01.parquet")
    
else:
    print(f"Failed to download file. Status code: {response.status_code}")

#-- Reading the Parquet file into a DataFrame --
df = pd.read_parquet("25.01.parquet")
""" print("Shape of the DataFrame:", df.shape)
print("DataFrame Columns:", df.columns) """

#-- Transforming the Data --
df_clean = df[(df["passenger_count"] > 0) & (df["passenger_count"] < 7)]
df_clean = df_clean[df_clean["trip_distance"] > 0]
df_clean = df_clean[df_clean["fare_amount"] > 0]
df_clean = df_clean[df_clean["total_amount"] > 0]
df_clean = df_clean.dropna(subset=["passenger_count", "trip_distance", "fare_amount", "total_amount", "tpep_pickup_datetime"])

""" print("Shape of the cleaned DataFrame:", df_clean.shape)
print("Number of rows dropped:", df.shape[0] - df_clean.shape[0]) """

#-- LOAD TO SQL --
conn = sqlite3.connect("nyc_taxi.db")
print("Connected to SQLite database.")
df_clean.to_sql("yellow_tripdata_2025_01", conn, if_exists="replace", index=False)
conn.close()
print("Data loaded into SQLite database successfully.")