CREATE PROCEDURE Dimension.PopStocks
AS
BEGIN

--Update Stocks where there have been changes
UPDATE Dimension.Stocks
SET Dimension.Stocks.StockName= b.StockName

FROM			Dimension.Stocks		a
INNER JOIN		Staging.Stocks	b on a.Symbol = b.Symbol

--Add New Stock News
INSERT Dimension.Stocks
SELECT a.*

FROM				Staging.Stocks	a
LEFT OUTER JOIN		Dimension.Stocks		b on a.Symbol = b.Symbol

WHERE b.Symbol is null

END