CREATE PROCEDURE Fact.PopStockPriceHistoryMinute
AS
BEGIN

INSERT Fact.StockPriceHistoryMinute
SELECT a.*

FROM				Staging.StockPriceHistoryMinute	a
LEFT OUTER JOIN		Fact.StockPriceHistoryMinute		b on a.Symbol = b.Symbol and a.Stocktime = b.Stocktime

WHERE b.Symbol is null

END