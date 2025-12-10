import duckdb
import os

# Persistent database file
con = duckdb.connect("project1.duckdb")  

DATA_DIR = "data"
OUTPUT_DIR = "output"

def run_etl():

    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

    # 1. Read raw CSV files
    con.execute(f"""
        CREATE OR REPLACE TABLE sales_raw AS 
        SELECT * FROM read_csv_auto('{DATA_DIR}/sales.csv');
    """)

    con.execute(f"""
        CREATE OR REPLACE TABLE customers_raw AS 
        SELECT * FROM read_csv_auto('{DATA_DIR}/customers.csv');
    """)

    con.execute(f"""
        CREATE OR REPLACE TABLE products_raw AS 
        SELECT * FROM read_csv_auto('{DATA_DIR}/products.csv');
    """)

    con.execute(f"""
        CREATE OR REPLACE TABLE stores_raw AS 
        SELECT * FROM read_csv_auto('{DATA_DIR}/stores.csv');
    """)

    # 2. Create Dimensions
    con.execute("""
        CREATE OR REPLACE TABLE dim_customers AS
        SELECT 
            customer_id,
            customer_name,
            age,
            city,
            gender
        FROM customers_raw;
    """)

    con.execute("""
        CREATE OR REPLACE TABLE dim_products AS
        SELECT 
            product_id,
            product_name,
            category,
            price,
            brand
        FROM products_raw;
    """)

    con.execute("""
        CREATE OR REPLACE TABLE dim_stores AS
        SELECT 
            store_id,
            store_name,
            city,
            state,
            manager
        FROM stores_raw;
    """)

    # 3. Create Fact Table
    con.execute("""
        CREATE OR REPLACE TABLE fact_sales AS
        SELECT
            sale_id,
            sales_raw.customer_id,
            sales_raw.product_id,
            sales_raw.store_id,
            quantity,
            sale_amount
        FROM sales_raw
        JOIN dim_customers USING (customer_id)
        JOIN dim_products USING (product_id)
        JOIN dim_stores USING (store_id);
    """)

    # 4. Export to Parquet
    con.execute(f"COPY dim_customers TO '{OUTPUT_DIR}/dim_customers.parquet' (FORMAT PARQUET);")
    con.execute(f"COPY dim_products TO '{OUTPUT_DIR}/dim_products.parquet' (FORMAT PARQUET);")
    con.execute(f"COPY dim_stores TO '{OUTPUT_DIR}/dim_stores.parquet' (FORMAT PARQUET);")
    con.execute(f"COPY fact_sales TO '{OUTPUT_DIR}/fact_sales.parquet' (FORMAT PARQUET);")

    print("ETL Completed Successfully. Parquet files created in output/")

if __name__ == "__main__":
    run_etl()
