CREATE PROCEDURE Fact.PopStockPriceHistoryDay
AS
BEGIN

INSERT Fact.StockPriceHistoryDay
SELECT a.*

FROM				Staging.StockPriceHistoryDay	a
LEFT OUTER JOIN		Fact.StockPriceHistoryDay		b on a.Symbol = b.Symbol and a.Stockdate = b.StockDate

WHERE b.Symbol is null

END