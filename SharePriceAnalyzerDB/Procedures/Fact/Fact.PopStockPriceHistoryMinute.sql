CREATE PROCEDURE Fact.PopStockPriceHistoryMinute
AS
BEGIN

INSERT Fact.StockPriceHistoryMinute
SELECT 

 a.Symbol
,a.Stockdatetime
,cast(a.Stockdatetime as date)
,cast(a.Stockdatetime as time)
,a.[Open]
,a.[High]
,a.[Low]
,a.[Close]
,a.[Volume]
,a.Dividends
,a.StockSplits

FROM				Staging.StockPriceHistoryMinute	a
LEFT OUTER JOIN		Fact.StockPriceHistoryMinute		b on a.Symbol = b.Symbol and a.Stockdatetime = b.Stockdatetime

WHERE b.Symbol is null

END