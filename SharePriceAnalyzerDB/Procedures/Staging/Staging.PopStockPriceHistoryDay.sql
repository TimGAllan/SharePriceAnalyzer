CREATE PROCEDURE Staging.PopStockPriceHistoryDay
AS
BEGIN

INSERT Staging.StockPriceHistoryDay
SELECT a.*

FROM				Increment.StockPriceHistoryDay	a
LEFT OUTER JOIN		Staging.StockPriceHistoryDay	b on a.Symbol = b.Symbol and a.Stockdate = b.Stockdate

WHERE b.Symbol is null

DELETE Increment.StockPriceHistoryDay

END