from controller import *
import time
import sys

star = [
	(0.7,  0.0),
	(2.0, -4.0),
	(3.3,  0.0),
	(0.0, -2.3),
	(4.0, -2.3),
	(0.7,  0.0)
]

box = [
	(0.0,  0.0),
	(4.0,  0.0),
	(4.0, -4.0),
	(0.0, -4.0),
	(0.0,  0.0)
]

c = Controller()
c.bot.penDown(c.dnspeed)
sys.exit(0)
c.drawPoints(box)
