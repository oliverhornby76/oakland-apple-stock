# Import required libraries
# Flask is used to create the web application
# jsonify converts Python objects into JSON responses
from flask import Flask, jsonify
import pyodbc

# Create Flask instance
app = Flask(__name__)

# Database connection configuration
SERVER = r"localhost"
DATABASE = "StockMarket"

# Connection string for SQL Server
CONN_STR = (
    "Driver={ODBC Driver 18 for SQL Server};"
    f"Server={SERVER};"
    f"Database={DATABASE};"
    "Trusted_Connection=yes;"
    "Encrypt=no;"
)

# Define API endpoint
@app.get("/prices/latest")
def latest_prices():
    
    # Establish connection to SQL Server
    with pyodbc.connect(CONN_STR) as conn:
        cur = conn.cursor()

        # Retrieve the latest 10 trading days for AAPL
        cur.execute("""
            SELECT TOP (10)
                Symbol, TradeDate, [Open], High, Low, [Close], Volume
            FROM AAPL.DailyPrice
            ORDER BY TradeDate DESC;
        """)

        rows = cur.fetchall()

    # Transform rows into JSON
    data = [
        {
            "symbol": r.Symbol,
            "tradeDate": str(r.TradeDate),
            "open": r.Open,
            "high": r.High,
            "low": r.Low,
            "close": r.Close,
            "volume": r.Volume,
        }
        for r in rows
    ]

    # Return JSON response
    return jsonify(data)

# Run the application in development mode
if __name__ == "__main__":
    app.run(debug=True)