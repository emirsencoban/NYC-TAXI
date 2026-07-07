import request
import pandas as pd
import pyarrow

#--Defining URL --
url = "https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2025-01.parquet"

response = request.get(url, stream=True)

if response.status_code == 200:
    print("File downloaded successfully.")
    ...


else:
    print(f"Failed to download file. Status code: {response.status_code}")