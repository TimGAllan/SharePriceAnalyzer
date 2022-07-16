CREATE PROCEDURE Staging.PopStocks
AS
BEGIN

--Update Stocks where there have been changes
UPDATE Staging.Stocks
SET Staging.Stocks.StockName= b.StockName

FROM			Staging.Stocks		a
INNER JOIN		Increment.Stocks	b on a.Symbol = b.Symbol

--Add New Stock News
INSERT Staging.Stocks
SELECT a.*

FROM				Increment.Stocks	a
LEFT OUTER JOIN		Staging.Stocks		b on a.Symbol = b.Symbol

WHERE b.Symbol is null

--Purage the Increment Table
DELETE Increment.Stocks

END