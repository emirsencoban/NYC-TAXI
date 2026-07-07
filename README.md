# NYC Yellow Taxi Data Pipeline (ETL)

A lightweight and efficient data engineering pipeline that automates the **Extract, Transform, Load (ETL)** process for the New York City (NYC) Yellow Taxi dataset. The pipeline handles millions of rows of data using memory-efficient streaming and database chunking techniques.

##  Architecture & Tech Stack
* **Python & UV:** Modern and fast environment/dependency management.
* **Pandas & PyArrow:** For memory-efficient processing of compressed `.parquet` big data files.
* **Requests:** For streaming large binary files directly from AWS S3 without overloading RAM.
* **SQLite & DBeaver:** Lightweight, relational SQL database engine for locally warehousing the cleaned dataset and executing analytics queries.

##  Pipeline Stages
1. **Extract:** Streams the official NYC Yellow Taxi Parquet file for `2025-01` in 8192-byte chunks to safely download without memory issues.
2. **Transform:** Filters out corrupted or anomalous rows (e.g., zero trip distances, unrealistic passenger counts, zero or negative fare amounts, and missing critical values). Cleaned approximately 2.8M valid trips while stripping ~650k anomaly records.
3. **Load:** Automatically opens a connection to a local SQLite database, creates/replaces the relational schema, and inserts the data.

##  Analytics Queries (Upcoming)
Database schemas are thoroughly queried using **DBeaver** to uncover hidden patterns such as:
* Top 5 highest tip-yielding locations (`PULocationID`).
* Peak hours for taxi ride density and fare distributions.

##  How to Run
Ensure you have `uv` installed, then run:
```bash
uv run main.py
