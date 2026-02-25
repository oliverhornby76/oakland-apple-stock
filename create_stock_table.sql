USE [StockMarket]
GO

/****** Object:  Table [AAPL].[DailyPrice]    Script Date: 25/02/2026 09:59:51 ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE TABLE [AAPL].[DailyPrice](
	[Symbol] [varchar](10) NOT NULL,
	[CompanyName] [varchar](20) NULL,
	[TradeDate] [date] NOT NULL,
	[Open] [float] NULL,
	[High] [float] NULL,
	[Low] [float] NULL,
	[Close] [float] NULL,
	[Volume] [bigint] NULL,
	[Source] [varchar](50) NOT NULL,
	[RecordProcessedBy] [sysname] NOT NULL,
	[RecordProcessedOn] [datetime2](0) NOT NULL,
 CONSTRAINT [PK_DailyPrice] PRIMARY KEY CLUSTERED 
(
	[Symbol] ASC,
	[TradeDate] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO

ALTER TABLE [AAPL].[DailyPrice] ADD  DEFAULT ('Apple Inc.') FOR [CompanyName]
GO

ALTER TABLE [AAPL].[DailyPrice] ADD  CONSTRAINT [DF_DailyPrice_Source]  DEFAULT ('AlphaVantage') FOR [Source]
GO

ALTER TABLE [AAPL].[DailyPrice] ADD  CONSTRAINT [DF_DailyPrice_SqlUserName]  DEFAULT (suser_sname()) FOR [RecordProcessedBy]
GO

ALTER TABLE [AAPL].[DailyPrice] ADD  CONSTRAINT [DF_DailyPrice_IngestedAtUtc]  DEFAULT (sysutcdatetime()) FOR [RecordProcessedOn]
GO


