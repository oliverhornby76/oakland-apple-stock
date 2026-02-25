# oakland-apple-stock
A simple data engineering project for Oakland that retrieves Apple stock data from a Alpha Vantage, stores it in SQL Server, and displays the results.

## Project Overview

This project demonstrates a basic data ingestion pipeline using Python to retrieve Apple stock data and load it into SQL Server. The steps taken are as follows:

1. Retrieve Apple stock data from Alpha Vantage's API
2. Storing the stock data inside a dedicated database within SQL Server

## Table Layout

Below is a screenshot showing the structure used to store the Apple stock data. A new database called StockMarket was created, along with a schema named AAPL, which represents the stock symbol for Apple. The approach taken is to create a separate schema for each stock where required. While it would also be possible to store multiple stocks in the same table with a symbol column to distinguish them, this design allows for more granular permission control at the schema level if needed.

![Pipeline Diagram](images/stockmarket_table.png)

## Schema

The SQL script used to create the table can be found [here](create_stock_table.sql).

The table stores one record per trading day for Apple (AAPL). Its purpose is to provide a high-level view of daily stock performance.


| Name | Description | Data Type | Notes |
|------|-------------|-----------|-------|
| Symbol | Stock symbol (AAPL for Apple Inc.) | varchar(10) |  |
| CompanyName | Company name | varchar(20) | Default value set to "Apple Inc." |
| TradeDate | Trading date | date | One row per trading day |
| Open | Opening price | float | Data type was chosen as it is suitable for continuously changing numerical data |
| High | Highest price | float | Data type was chosen as it is suitable for continuously changing numerical data |
| Low | Lowest price | float | Data type was chosen as it is suitable for continuously changing numerical data |
| Close | Closing price | float | Data type was chosen as it is suitable for continuously changing numerical data |
| Volume | Number of shares traded | bigint | Data type was chosen as it can safely handle high numbers without risk of overflow |
| Source | Data source | varchar(50) | Default value set to "AlphaVantage" |
| RecordProcessedBy | SQL username | sysname | Auto populated to track who/what inserted or upserted the data |
| RecordProcessedOn | Processing timestamp | datetime2 | UTC timestamp of insert/upsert event |

The composite primary key on Symbol and TradeDate ensures that only one record exists for each stock on a given trading day, helping prevent duplicates and maintain data integrity.
