import FetchStockPriceHistory as sh
import FetchStockInfo as info

StockSymbols = ['ADEN.SW','RAND.AS','MAN','HAS.L','RCRRF','2181.T','RHI','KELYA']

for x in StockSymbols:
	info.FetchStockInfo(x)
	sh.FetchStockPriceHistoryMinute(x)
	sh.FetchStockPriceHistoryDay(x)
