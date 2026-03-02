SELECT      COUNT(DISTINCT RecordProcessedOn) AS Result


FROM        [StockMarket].[AAPL].[DailyPrice]

WHERE       CONVERT(DATE,RecordProcessedOn) = CONVERT(DATE,GETDATE())