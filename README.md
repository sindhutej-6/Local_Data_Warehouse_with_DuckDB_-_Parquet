
# **README.md**

#  Local Data Warehouse Project using DuckDB

##  Overview

This project demonstrates how to build a **local high-performance data warehouse** using **DuckDB**.
It follows a complete **ETL → Transformation → Star Schema → Parquet Export → Analytics → Benchmarking** workflow.

The goal is to show how modern data engineering pipelines can be built efficiently on local systems using columnar storage and analytical databases.

-----------------------------------------------------------------------------------------------------------------------------------------------------

##  Objectives

This project accomplishes the following:

* Ingest multiple CSV files containing sales-related data
* Transform the raw data into a **Star Schema**
* Create **Fact** and **Dimension** tables
* Export the final model as **Parquet** files
* Run **analytical SQL queries** on the warehouse
* Benchmark **CSV vs Parquet performance**
* Generate a performance report

--------------------------------------------------------------------------------------------------------------------------------------------------

##  Project Structure

```
project-1/
│── data/                     # Input CSV files
│── output/                   # Generated Parquet files
│── scripts/                  # ETL pipeline, Benchmark, Analytical SQL queries
│── performance_report.md     # Benchmark results
│── requirements.txt          # Python dependencies
│── README.md                 # Project documentation
```
------------------------------------------------------------------------------------------------------------------------------------------------

##  Data Model — Star Schema

### **Fact Table**

#### `fact_sales`

Contains measurable business facts:

* sale_id
* customer_id
* product_id
* store_id
* quantity
* sale_amount


### **Dimension Tables**

#### `dim_customers`

* customer_id
* customer_name
* age
* city
* gender

#### `dim_products`

* product_id
* product_name
* category
* price
* brand

#### `dim_stores`

* store_id
* store_name
* city
* state
* manager

---------------------------------------------------------------------------------------------------------------

##  Environment Setup

### 1. Install Python Dependencies

Create a file named **requirements.txt**:


duckdb
pandas
pyarrow


Install all dependencies:

pip install -r requirements.txt


----------------------------------------------------------------------------------------------------------

##  Running the Entire Pipeline (Start → End)

### **1. Place CSV Files**

Put the following into `/data`:


customers.csv
products.csv
stores.csv
sales.csv


### **2. Run ETL Pipeline**

This will:

* Load CSVs
* Create fact & dimensions
* Write Parquet files to `/output`

Run:

python scripts/etl.py


You will see:

ETL Completed Successfully. Parquet files created in output/


### **3. Run Analytical Queries**
##  Persistent DuckDB Database (`project1.duckdb`)

The file **`project1.duckdb`** is used to make our DuckDB tables **persistent**, instead of temporary in-memory tables.

### **Purpose**

a). **Persistent Storage of Tables**

   * Tables like `fact_sales`, `dim_customers`, `dim_products`, and `dim_stores` are stored on disk.
   * This allows you to close Python or DuckDB shell and still keep all tables for future use.


Open DuckDB:


duckdb .\project1.duckdb


Run queries:
.read scripts/queries.sql


### **4. Benchmark CSV vs Parquet Performance**

The benchmark.py script measures and compares the execution time of the same analytical queries on raw CSV files versus Parquet files. Parquet is columnar and optimized for analytics, so queries run significantly faster, demonstrating the performance advantage of using Parquet over CSV.



## Output — Parquet Files

The ETL will generate:

```
output/dim_customers.parquet
output/dim_products.parquet
output/dim_stores.parquet
output/fact_sales.parquet
```

These files are highly optimized, columnar, and ready for fast analytics.

Note: Parquet files are binary columnar files, so don't open them in Notepad — they will always look encoded or unreadable.
      Use VS code Extension: "Parquet Viewer" then it shows data in the form JSON.


-------------------------------------------------------------------------------------------------------------------------------------------------------------------------

##  Key Learnings

* How ETL pipelines are built using DuckDB
* Importance of star schema modeling
* Why Parquet is faster than CSV
* How to benchmark performance of analytical queries
* Benefits of columnar storage and vectorized execution

----------------------------------------------------------------------------------------------------------------------------------------------------------------------

##  Summary

This project fully demonstrates:

* End-to-end ETL
* Data modeling
* Parquet optimization
* Analytical SQL
* Benchmarking and performance reporting

It provides a strong foundation for data engineering and analytical workflows.




