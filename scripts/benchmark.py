import duckdb
import time

def timer(query):
    start = time.time()
    duckdb.query(query).fetchall()
    return round(time.time() - start, 4)

def run_benchmarks():
    queries = [
        "SELECT * FROM read_csv_auto('data/sales.csv') LIMIT 50000;",
        "SELECT * FROM 'output/fact_sales.parquet' LIMIT 50000;",
    ]

    print("\n--- Benchmarking ---")
    results = []

    for q in queries:
        t = timer(q)
        results.append((q[:40] + "...", t))

    print("\nResults:")
    for name, t in results:
        print(f"{name} => {t} seconds")

if __name__ == "__main__":
    run_benchmarks()
