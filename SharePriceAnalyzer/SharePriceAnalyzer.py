import FetchStockPriceHistory as sh
import FetchStockInfo as info
import datetime as dt
import time
import keyboard
import sys

def exitCheck():
	if keyboard.is_pressed("esc"):
		print(dt.datetime.now().strftime("%H:%M:%S"), "Stopping...")
		sys.exit()

def Main():
	StockSymbols = ['ADEN.SW','RAND.AS','MAN','HAS.L','RHI','KELYA']

	for x in StockSymbols:
		info.FetchStockInfo(x)
		sh.FetchStockPriceHistoryDay(x)
		exitCheck()

	i = 0

	while True:
		
		if i <= 0:
			for x in StockSymbols:	
				sh.FetchStockPriceHistoryMinute(x)
				exitCheck()

			i = 60
	
		i -= 1
	
		if i % 5 == 0 and i>=1:
			print(dt.datetime.now().strftime("%H:%M:%S"), "Updating Live prices in", i, "seconds...")

		exitCheck()	

		time.sleep(1)

Main()