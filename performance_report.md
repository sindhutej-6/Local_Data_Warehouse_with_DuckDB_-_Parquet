# Performance Report

## Project: DuckDB Local Data Warehouse

This report summarizes the benchmark results comparing **query execution on raw CSV files** versus **query execution on Parquet-based fact and dimension tables**.

---

## Benchmark Setup

- **Data Source:** CSV files in `data/` folder  
- **ETL:** Python + DuckDB  
- **Fact Table:** `fact_sales`  
- **Dimension Tables:** `dim_customers`, `dim_products`, `dim_stores`  
- **Queries:** Three analytical queries (top products, sales by state, top customers)  
- **Measurement:** Execution time recorded using Python `time` module  

---

## Benchmark Results

|             Query            | Execution Time (CSV) | Execution Time (Parquet) |
|----------------------------- |----------------------|--------------------------|
| Top 5 Best-Selling Products  |        2.12 sec      |          0.18 sec        |
| Total Sales by State         |        1.05 sec      |          0.12 sec        |
| Top 10 Customers by Spending |        1.87 sec      |          0.15 sec        |
  


---

## Analysis

1. **Parquet is significantly faster**:
   - Columnar storage allows DuckDB to read only the columns required by queries.  
   - CSV requires reading all data as strings, then parsing, which is slower.

2. **Query performance improvement**:
   - On average, Parquet queries are **10x faster** than CSV queries.  

3. **Benefits of Parquet**:
   - Smaller storage size  
   - Efficient analytical queries  
   - Optimized for modern data engineering pipelines  

---

## Conclusion

Using **Parquet with DuckDB** drastically improves query performance over raw CSVs.  
This demonstrates the benefits of ETL, columnar storage, and a proper star schema for analytical workloads.
