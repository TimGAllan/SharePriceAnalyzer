import yfinance as yf
import pandas as pd
import pyodbc
import sqlalchemy
import datetime as dt

def FetchStockInfo(symbol):
	ticker = yf.Ticker(symbol)
	a = ticker.info
	conn_str = (
	r'DRIVER={SQL Server Native Client 11.0};'
	r'SERVER=LAPTOP-7T05M45R\TIM2019;'
	r'DATABASE=SharePriceAnalyzerDB;'
	r'Trusted_Connection=yes;'
	)

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