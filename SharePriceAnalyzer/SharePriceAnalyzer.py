import FetchStockPriceHistory as sh
import FetchStockInfo as info
import time

StockSymbols = ['ADEN.SW','RAND.AS','MAN','HAS.L','RHI','KELYA']

for x in StockSymbols:
	info.FetchStockInfo(x)
	sh.FetchStockPriceHistoryDay(x)

running = 1

while running:
	for x in StockSymbols:	
		sh.FetchStockPriceHistoryMinute(x)
		
	time.sleep(60)