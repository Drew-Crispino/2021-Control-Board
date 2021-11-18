import digitalio
import time
import board
from digitalio import DigitalInOut, Direction, Pull
from analogio import AnalogIn
import neopixel

"""Buttons: 25"""
btn1 = digitalio.DigitalInOut(board.D1)
btn2 = digitalio.DigitalInOut(board.D2)
btn3 = digitalio.DigitalInOut(board.D3)
btn4 = digitalio.DigitalInOut(board.D4)
btn5 = digitalio.DigitalInOut(board.D5)
btn6 = digitalio.DigitalInOut(board.D6)
btn7 = digitalio.DigitalInOut(board.D7)
btn8 = digitalio.DigitalInOut(board.D8)
btn9 = digitalio.DigitalInOut(board.D9)
btn10 = digitalio.DigitalInOut(board.D10)
btn11 = digitalio.DigitalInOut(board.D11)
btn12 = digitalio.DigitalInOut(board.D12)
btn13 = digitalio.DigitalInOut(board.D13)
btn14 = digitalio.DigitalInOut(board.D14)
btn15 = digitalio.DigitalInOut(board.D15)
btn16 = digitalio.DigitalInOut(board.D16)
btn17 = digitalio.DigitalInOut(board.D17)
btn18 = digitalio.DigitalInOut(board.D18)
btn19 = digitalio.DigitalInOut(board.D19)
btn20 = digitalio.DigitalInOut(board.D20)
btn21 = digitalio.DigitalInOut(board.D21)
btn22 = digitalio.DigitalInOut(board.D22)
btn23 = digitalio.DigitalInOut(board.D23)
btn24 = digitalio.DigitalInOut(board.D24)
btn25 = digitalio.DigitalInOut(board.D25)

buttons = [btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9, btn10,
btn11, btn12, btn13, btn14, btn15, btn16, btn17, btn18, btn19, btn20,
btn21, btn22, btn23, btn24, btn25]

for x in buttons:
    x.direction = digitalio.Direction.INPUT
    x.pull = digitalio.Pull.DOWN

"""Switches: 25"""
switch1 = digitalio.DigitalInOut(board.D26)
switch2 = digitalio.DigitalInOut(board.D27)
switch3 = digitalio.DigitalInOut(board.D28)
switch4 = digitalio.DigitalInOut(board.D29)
switch5 = digitalio.DigitalInOut(board.D30)
switch6 = digitalio.DigitalInOut(board.D31)
switch7 = digitalio.DigitalInOut(board.D32)
switch8 = digitalio.DigitalInOut(board.D33)
switch9 = digitalio.DigitalInOut(board.D34)
switch10 = digitalio.DigitalInOut(board.D35)
switch11 = digitalio.DigitalInOut(board.D36)
switch12 = digitalio.DigitalInOut(board.D37)
switch13 = digitalio.DigitalInOut(board.D38)
switch14 = digitalio.DigitalInOut(board.D39)
switch15 = digitalio.DigitalInOut(board.D40)
switch16 = digitalio.DigitalInOut(board.D41)
switch17 = digitalio.DigitalInOut(board.D42)
switch18 = digitalio.DigitalInOut(board.D43)
switch19 = digitalio.DigitalInOut(board.D44)
switch20 = digitalio.DigitalInOut(board.D45)
switch21 = digitalio.DigitalInOut(board.D46)
switch22 = digitalio.DigitalInOut(board.D47)
switch23 = digitalio.DigitalInOut(board.D48)
switch24 = digitalio.DigitalInOut(board.D49)
switch25 = digitalio.DigitalInOut(board.D50)

switches = [switch1, switch2, switch3, switch4, switch5,
switch6, switch7, switch8, switch9, switch10,
switch11, switch12, switch13, switch14, switch15,
switch16, switch17, switch18, switch19, switch20,
switch21, switch22, switch23, switch24, switch25,]

for x in switches:
    x.direction = digitalio.Direction.INPUT
    x.pull = digitalio.Pull.DOWN

"""Dials: 10"""
dial1 = AnalogIn(board.A0)
dial2 = AnalogIn(board.A1)
dial3 = AnalogIn(board.A2)
dial4 = AnalogIn(board.A3)
dial5 = AnalogIn(board.A4)
dial6 = AnalogIn(board.A5)
dial7 = AnalogIn(board.A6)
dial8 = AnalogIn(board.A7)
dial9 = AnalogIn(board.A8)
dial10 = AnalogIn(board.A9)

dials = [dial1, dial2, dial3, dial4, dial5, dial6, dial7, dial8, dial9, dial10]
