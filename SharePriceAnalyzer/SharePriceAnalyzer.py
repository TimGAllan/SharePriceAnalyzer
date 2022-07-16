
import FetchStockPriceHistoryMinute as hist
import FetchStockInfo as info

StockSymbols = ['ADEN.SW','RAND.AS','MAN','HAS.L','RCRRF','2181.T','RHI','KELYA']

for x in StockSymbols:
	info.FetchStockInfo(x)
	hist.FetchStockPriceHistoryMinute(x)
