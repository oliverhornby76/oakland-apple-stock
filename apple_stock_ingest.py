# Enables API calls
import requests

# Enables date conversion
from datetime import datetime

# Enables connection between Python and SQL Server
import pyodbc

# Alpha Advantage API key
API_KEY = "EEAMGVQPUNG5SCK0"

# Apple Inc. symbol to pull Apple stock data
SYMBOL = "AAPL"

# Send a HTTPS Get request to the Alpha Vantage API
data = requests.get(
    "https://www.alphavantage.co/query",
    params={"function": "TIME_SERIES_DAILY", "symbol": SYMBOL, "apikey": API_KEY},
).json()

# Extracting only the daily time series data from the API response
series = data["Time Series (Daily)"]

# Defining the SQL Server Connection with key parameters
conn_str = (
    "DRIVER={ODBC Driver 18 for SQL Server};"
    "SERVER=localhost;"
    "DATABASE=StockMarket;"
    "Trusted_Connection=yes;"
    "Encrypt=yes;"
    "TrustServerCertificate=yes;"
)

# SQL statement used to perform upsert (update if exists (only if the symbol and trade date match), insert if not).
UPSERT_SQL = """
UPDATE StockMarket.AAPL.DailyPrice
SET    [Open]  = ?,
       [High]  = ?,
       [Low]   = ?,
       [Close] = ?,
       Volume  = ?

WHERE  Symbol = ?
  AND  [TradeDate] = ?;

IF @@ROWCOUNT = 0
BEGIN
    INSERT INTO StockMarket.AAPL.DailyPrice (Symbol, [TradeDate], [Open], [High], [Low], [Close], Volume)
    VALUES (?, ?, ?, ?, ?, ?, ?);
END
"""

# References the SQL connection above
with pyodbc.connect(conn_str) as conn:
    cur = conn.cursor()

    for date_str, vals in series.items():
        # Convert date to yyyy-mm-dd format
        d = datetime.strptime(date_str, "%Y-%m-%d").date()

        # Convert data to float 
        o = float(vals["1. open"])
        h = float(vals["2. high"])
        l = float(vals["3. low"])
        c = float(vals["4. close"])

        # Convert data to float 
        v = int(vals["5. volume"])

        cur.execute(UPSERT_SQL, (o, h, l, c, v, SYMBOL, d, SYMBOL, d, o, h, l, c, v))

    # Saves changes
    conn.commit()

# Displays confirmation message of volume of rows processed
print(f"Upserted {len(series)} rows for {SYMBOL}")