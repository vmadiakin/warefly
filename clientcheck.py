from clickhouse_driver import Client

client = Client(host='localhost', port=9000)

try:
    client.execute("SELECT 1")
    print("ClickHouse is available.")
except Exception as e:
    print(f"Error connecting to ClickHouse: {e}")
finally:
    client.disconnect()
