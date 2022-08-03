import FetchStockPriceHistory as sh
import FetchStockInfo as info
import datetime as dt
import time
import keyboard
import sys

StockSymbols = ['ADEN.SW','RAND.AS','MAN','HAS.L','RHI','KELYA']

for x in StockSymbols:
	info.FetchStockInfo(x)
	sh.FetchStockPriceHistoryDay(x)

i = 0

while True:
		
	if i <= 0:
		for x in StockSymbols:	
			sh.FetchStockPriceHistoryMinute(x)

		i = 60

	i -= 1
	
	if i % 5 == 0 and i>=1:
		print(dt.datetime.now().strftime("%H:%M:%S"), "Updating Live prices in", i, "seconds...")

	if keyboard.read_key() == "esc":
		print(dt.datetime.now().strftime("%H:%M:%S"), "Stopping...")
		sys.exit()		

	time.sleep(1)

