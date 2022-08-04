CREATE VIEW vw_Live_Price_Summary
AS
with LastClose 
as (
    SELECT Symbol, max(StockDatetime) As StockDatetime, cast(max(StockDatetime) as date) As StockDate
    FROM Fact.StockPriceHistoryMinute
    GROUP BY Symbol
)

,DailyStats 
as (
    SELECT      a.Symbol, sum(Volume) As Volume, min([Close]) As Low, max([Close]) As High
    FROM        Fact.StockPriceHistoryMinute a
    INNER JOIN  LastClose b on a.Symbol = b.Symbol and a.StockDate = b.StockDate
    GROUP BY    a.Symbol

)

,OpenPrice 
as (
    SELECT      a.Symbol, [Close] As OpenPrice, ROW_NUMBER() OVER(PARTITION BY a.Symbol ORDER BY a.StockDatetime ASC) As Roww
    FROM        Fact.StockPriceHistoryMinute a
    INNER JOIN  LastClose b on a.Symbol = b.Symbol and a.StockDate = b.StockDate
)
,YearStats
as (
    SELECT a.Symbol, max(a.[Close]) as [52WkHigh], min(a.[Close]) As [52WkLow]
    FROM        Fact.StockPriceHistoryDay       a
    INNER JOIN  Fact.StockPriceHistoryMinute    b on a.Symbol = b.Symbol and a.StockDate between dateadd(yy,-1,b.StockDate) and b.StockDate
    GROUP BY    a.Symbol

)


SELECT 

a.Symbol 
,aa.StockName
,a.StockDatetime
,a.StockDate
,a.Stocktime
,aa.Currency
,a.[Close]          As CurrentPrice
,d.OpenPrice
,c.High
,c.Low
,e.[52WkHigh]
,e.[52WkLow]
,c.Volume

FROM        Fact.StockPriceHistoryMinute    a
INNER JOIN  Dimension.Stocks                aa on a.Symbol = aa.Symbol
INNER JOIN  LastClose                       b  on a.Symbol = b.Symbol and a.Stockdatetime = b.StockDatetime
INNER JOIN  DailyStats                      c  on a.Symbol = c.Symbol
INNER JOIN  OpenPrice                       d  on a.Symbol = d.Symbol and d.Roww = 1
INNER JOIN  YearStats                       e  on a.Symbol = e.Symbol