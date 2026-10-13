from database import run_query

columns, rows = run_query(
    "SELECT COUNT(*) FROM customers"
)

print("Customer count:", rows[0][0])

columns, rows = run_query(
    "SELECT SUM(price) FROM order_items"
)

print("Total revenue:", rows[0][0])