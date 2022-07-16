import yfinance as yf
import pandas as pd
import pyodbc
import sqlalchemy
import datetime as dt

def FetchStockPriceHistoryMinute(Stocksymbol):
	fromDate = dt.datetime.today() + dt.timedelta(days = -6)
	fromDate = fromDate.strftime('%Y-%m-%d')

	toDate = dt.datetime.today() + dt.timedelta(days = 1)
	toDate = toDate.strftime('%Y-%m-%d')

	ticker = yf.Ticker(Stocksymbol)
	df = ticker.history(start=fromDate, end=toDate, interval='1m')
	df = df.reset_index(level=0)
	df['Symbol'] = Stocksymbol

	df.columns = ['Stocktime','Open','High','Low','Close','Volume','Dividends','StockSplits','Symbol']

	conn_str = (
		r'DRIVER={SQL Server Native Client 11.0};'
		r'SERVER=LAPTOP-7T05M45R\TIM2019;'
		r'DATABASE=SharePriceAnalyzerDB;'
		r'Trusted_Connection=yes;'
	)

	cnxn = pyodbc.connect(conn_str)
	cursor = cnxn.cursor()

	cursor.execute('DELETE Increment.StockPriceHistoryMinute')
	cnxn.commit()

	for index,row in df.iterrows():
		cursor.execute('INSERT Increment.StockPriceHistoryMinute([Symbol],[Stocktime],[Open],[High],[Low],[Close],[Volume],[Dividends],[StockSplits]) values (?,?,?,?,?,?,?,?,?)', 
						row['Symbol'], 
						row['Stocktime'], 
						row['Open'],
						row['High'],
						row['Low'],
						row['Close'],
						row['Volume'],
						row['Dividends'],
						row['StockSplits'])
		cnxn.commit()

	print(Stocksymbol)

	cursor.execute('EXEC Staging.PopStockPriceHistoryMinute')
	cnxn.commit()

	cursor.execute('EXEC Fact.PopStockPriceHistoryMinute')
	cnxn.commit()
	cursor.close()
	cnxn.close()
