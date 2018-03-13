## Unit 5 Project - Gas Pump
## Computer Programming II - Gavin Weiss


## Libraries
import time
import random
import simpleguitk as simplegui


##> Define Global Variables
gallons = 0
price = 0

StationLabel = "Shell"
GallonLabel = "Gallons: "
PriceLabel= "Price: "


##> Define Helper Functions
def GallonInc():

	global gallons
	global price

	gallons = gallons + 0.01

	gallons = round(gallons, 2)

	GallonTimer.start()

	return gallons
	return price

	
def StandardFuel():

	global gallons
	global price

	price = gallons * 1.5

	price = round(price, 2)

	GallonInc()
	StandardPriceTimer.start()


def PremiumFuel():

	global gallons
	global price

	price = gallons * 1.7

	price = round(price, 2)

	GallonInc()
	PremiumPriceTimer.start()


def Stop():

	global gallons
	global price

	GallonTimer.stop()
	StandardPriceTimer.stop()


##> Define Classes



##> Define Event Handlers
def draw(canvas):

	canvas.draw_text(str(gallons), [120, 100], 12, "Grey", "Monospace")
	canvas.draw_text(str(price), [120, 150], 12, "Green", "Monospace")
	
	canvas.draw_text(StationLabel, [20, 50], 14, "Yellow", "Monospace")
	canvas.draw_text(GallonLabel, [20, 100], 12, "Grey", "Monospace")
	canvas.draw_text(PriceLabel, [20, 150], 12, "Green", "Monospace")
	



##> Create Frame
frame = simplegui.create_frame("SimpleGUI", 300, 200)
GallonTimer = simplegui.create_timer(500, GallonInc)
StandardPriceTimer = simplegui.create_timer(500, StandardFuel)
PremiumPriceTimer = simplegui.create_timer(500, PremiumFuel)



##> Register Event Handlers
frame.set_draw_handler(draw)
StandardFuelButton = frame.add_button("Standard", StandardFuel)
PremiumFuelButton = frame.add_button("Premium", PremiumFuel)
StopButton = frame.add_button("Stop", Stop)


##> Start Frame and Timers
frame.start()
