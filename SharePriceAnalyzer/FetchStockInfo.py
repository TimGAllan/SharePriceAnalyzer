import yfinance as yf
import pyodbc
import datetime as dt

def FetchStockInfo(Stocksymbol):
	ticker = yf.Ticker(Stocksymbol)
	a = ticker.info
	conn_str = (
	r'DRIVER={SQL Server Native Client 11.0};'
	r'SERVER=LAPTOP-7T05M45R\TIM2019;'
	r'DATABASE=SharePriceAnalyzerDB;'
	r'Trusted_Connection=yes;'
	)

	print(dt.datetime.now().strftime("%H:%M:%S"),"Updating Stock Info for " + Stocksymbol)

	cnxn = pyodbc.connect(conn_str)
	cursor = cnxn.cursor()

	cursor.execute('INSERT Increment.Stocks([Symbol],[StockName],[Currency]) values (?,?,?)', 
				a['symbol'], 
				a['longName'],
				a['financialCurrency'])
	cnxn.commit()

	cursor.execute('EXEC Staging.PopStocks')
	cnxn.commit()

	cursor.execute('EXEC Dimension.PopStocks')
	cnxn.commit()

	cursor.close()
	cnxn.close()