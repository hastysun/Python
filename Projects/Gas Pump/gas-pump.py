## Unit 5 Project - Gas Pump Version 2
## Computer Programming II - Gavin Weiss 

## Due Thursday

## Libraries
import time
import random
import simpleguitk as simplegui


## Global Variables
gallons = 0
price = 0
FuelType = 0

StationLabel = "Shell"
GallonLabel = "Gallons: "
PriceLabel = "Price: "
DollarSignLabel = "$"



## Functions
def GallonInc():

    global gallons, price

    gallons = gallons + 0.001

    gallons = round(gallons, 3)

    return gallons, price, FuelType


def StandardFuel():

    global gallons, price, FuelType

    FuelType = 1

    price = gallons * 2.49

    price = round(price, 2)

    Message.set_text("\n Standard Fuel Selected \n")

    return gallons, price, FuelType


def PlusFuel():

    global gallons, price, FuelType

    FuelType = 2

    price = gallons * 3.75

    price = round(price, 2)

    Message.set_text("\n Plus Fuel Selected \n")
    
    return gallons, price, FuelType


def PremiumFuel():

    global gallons, price, FuelType

    FuelType = 3

    price = gallons * 4.29

    price = round(price, 2)

    Message.set_text("\n Premium Fuel Selected \n")

    return gallons, price, FuelType


def Start():

    global gallons
    global price
    global FuelType


    print(FuelType)

    if FuelType == 0:

        Message.set_text("\n Error: Please select a fuel type. \n")

        return

    if FuelType == 1:

        GallonTimer.start()
        StandardPriceTimer.start()

        return

    if FuelType == 2:

        GallonTimer.start()
        PlusPriceTimer.start()

    if FuelType == 3:

        GallonTimer.start()
        PremiumPriceTimer.start()

        return

    return


def Stop():

    if FuelType == 0:

        Message.set_text("\n Error: No fuel type selected. \n")

        return

    if FuelType == 1:

        Message.set_text("\n Pump Stopped. \n")

        GallonTimer.stop()
        StandardPriceTimer.stop()

        return

    if FuelType == 2:

        Message.set_text("\n Pump Stopped. \n")

        GallonTimer.stop()
        PlusPriceTimer.stop()

    if FuelType == 3:

        Message.set_text("\n Pump Stopped. \n")

        GallonTimer.stop()
        PremiumPriceTimer.stop()

        return

    return


def Reset():

    global gallons, price, FuelType

    gallons = 0
    price = 0
    FuelType = 0

    GallonTimer.stop()
    StandardPriceTimer.stop()
    PlusPriceTimer.stop()
    PremiumPriceTimer.stop()

    Message.set_text("\n Pump Reset \n")

    return gallons, price, FuelType


def Spacer():

    return



## Event Handlers
def draw(canvas):

    canvas.draw_text(str(gallons), [120, 125], 12, "Grey", "Monospace")
    canvas.draw_text(str(price), [120, 175], 12, "Green", "Monospace")

    canvas.draw_text(StationLabel, [20, 50], 14, "Yellow", "Monospace")
    canvas.draw_text(GallonLabel, [20, 125], 12, "Grey", "Monospace")
    canvas.draw_text(PriceLabel, [20, 175], 12, "Green", "Monospace")
    canvas.draw_text(DollarSignLabel, [100, 175], 12, "Green", "Monospace")



## Frame
frame = simplegui.create_frame("SimpleGUI", 400, 300)

GallonTimer = simplegui.create_timer(10, GallonInc)
StandardPriceTimer = simplegui.create_timer(100, StandardFuel)
PlusPriceTimer = simplegui.create_timer(100, PlusFuel)
PremiumPriceTimer = simplegui.create_timer(100, PremiumFuel)

Message = frame.add_label("Label")
Message.set_text(
        "\n Welcome to the Shell gas station. \n"
        "\n Please Select a fuel type \n"
        )

Spacer = frame.add_label("")
Spacer.set_text("")



## Init Event Handlers
frame.set_draw_handler(draw)
StandardFuelButton = frame.add_button("Standard - $2.49", StandardFuel, 50)
PlusFuelButton = frame.add_button("Plus - $3.75", PlusFuel, 50)
PremiumFuelButton = frame.add_button("Premium - $4.29", PremiumFuel, 50)

SpacerButton = frame.add_button("", Spacer, 50)

StartButton = frame.add_button("Start", Start, 50)
StopButton = frame.add_button("Stop", Stop, 50)
ResetButton = frame.add_button("Reset", Reset, 50)



## Init
frame.start()
