import FetchStockPriceHistory as sh
import FetchStockInfo as info
import datetime as dt
import time
import keyboard
import sys

# If the Esc Key is pressed, exit immediately.
def exitCheck():
	if keyboard.is_pressed("esc"):
		print(dt.datetime.now().strftime("%H:%M:%S"), "Stopping...")
		sys.exit()

def Main():

	# Change the line below to include different Stocks
	StockSymbols = ['ADEN.SW','RAND.AS','MAN','HAS.L','RHI','KELYA']

	# Collect Stock Meta Information and Stock Daily History
	for x in StockSymbols:
		info.FetchStockInfo(x)
		sh.FetchStockPriceHistoryDay(x)
		exitCheck()

	i = 0

	# Collect Stock Live Information
	while True:
		
		if i <= 0:
			for x in StockSymbols:	
				sh.FetchStockPriceHistoryMinute(x)
				exitCheck()
			
			# Reset the timer to 60
			i = 60
	
		i -= 1
	
		# Print the remaing second until the next API call every 5 seconds.
		if i % 5 == 0 and i>=1:
			print(dt.datetime.now().strftime("%H:%M:%S"), "Updating Live prices in", i, "seconds...")

		exitCheck()	

		# Wait 1 second.
		time.sleep(1)

Main()