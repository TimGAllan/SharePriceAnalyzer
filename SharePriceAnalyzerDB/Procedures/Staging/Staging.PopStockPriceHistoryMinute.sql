CREATE PROCEDURE Staging.PopStockPriceHistoryMinute
AS
BEGIN

INSERT Staging.StockPriceHistoryMinute
SELECT a.*

FROM				Increment.StockPriceHistoryMinute	a
LEFT OUTER JOIN		Staging.StockPriceHistoryMinute		b on a.Symbol = b.Symbol and a.Stocktime = b.Stocktime

WHERE b.Symbol is null

DELETE Increment.StockPriceHistoryMinute

END