import requests
import pandas as pd
import pyarrow

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
print("Shape of the DataFrame:", df.shape)
print("DataFrame Columns:", df.columns)