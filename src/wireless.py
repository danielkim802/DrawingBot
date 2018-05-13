import socket
from bot import *
import sys

# Commands
BOT_FORWARD        = 0
BOT_ROTATE         = 1
BOT_STOP           = 2
BOT_ADJUST         = 3
BOT_PENUP          = 4
BOT_PENDOWN        = 5
BOT_ROTATE_ADJUST  = 6
BOT_FORWARD_ADJUST = 7
BOT_TRIM_LEFT      = 8
BOT_TRIM_RIGHT     = 9

# Comm constants
PACKET_SIZE        = 50
IP_ADDR            = '192.168.43.28'
PORT               = 5005

class VirtualBotTX(object):
	def __init__(self, ip=IP_ADDR, port=PORT):
		self.pen = False
		self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
		self.s.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
		self.s.bind((ip, port))
		self.s.listen(1)
		self.conn, self.addr = self.s.accept()
		print 'Connected to:', self.addr

	def close(self):
		self.conn.close()

	def makePacket(self, cmd, arg):
		packet = "%i %f" % (cmd, arg)
		packet += " " * (PACKET_SIZE - 1 - len(packet)) + '\n'
		return packet

	def rotate(self, i):
		self.conn.send(self.makePacket(BOT_ROTATE, i))
	
	def rotateAdjust(self, i):
		self.conn.send(self.makePacket(BOT_ROTATE_ADJUST, i))

	def forward(self, i):
		self.conn.send(self.makePacket(BOT_FORWARD, i))
	
	def forwardAdjust(self, i):
		self.conn.send(self.makePacket(BOT_FORWARD_ADJUST, i))

	def adjust(self, dx):
		self.conn.send(self.makePacket(BOT_ADJUST, dx))

	def penDown(self, i):
		self.conn.send(self.makePacket(BOT_PENDOWN, i))
		self.pen = True

	def penUp(self, i):
		self.conn.send(self.makePacket(BOT_PENUP, i))
		self.pen = False

	def trimLeft(self, i):
		self.conn.send(self.makePacket(BOT_TRIM_LEFT, i))

	def trimRight(self, i):
		self.conn.send(self.makePacket(BOT_TRIM_RIGHT, i))

	def stop(self):
		self.conn.send(self.makePacket(BOT_STOP, 0))

class VirtualBotRX(object):
	def __init__(self, ip=IP_ADDR, port=PORT):
		self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.s.connect((ip, port))
		self.bot = Bot()
		print 'Connected!'

	def getCommand(self):
		line = self.s.recv(50)
		if line == '':
			sys.exit(0)
		cmd, arg = line.split()
		return int(cmd), float(arg)

	def execute(self, cmd):
		cmd, arg = cmd
		if cmd == BOT_FORWARD:
			print "BOT_FORWARD:", arg
			self.bot.forward(arg)
		elif cmd == BOT_ROTATE:
			print "BOT_ROTATE:", arg
			self.bot.rotate(arg)
		elif cmd == BOT_STOP:
			print "BOT_STOP:", arg
			self.bot.stop()
		elif cmd == BOT_ADJUST:
			print "BOT_ADJUST:", arg
			self.bot.adjust(arg)
		elif cmd == BOT_PENUP:
			print "BOT_PENUP:", arg
			self.bot.penUp(arg)
		elif cmd == BOT_PENDOWN:
			print "BOT_PENDOWN:", arg
			self.bot.penDown(arg)
		elif cmd == BOT_ROTATE_ADJUST:
			print "BOT_ROTATE_ADJUST:", arg
			self.bot.rotateAdjust(arg)
		elif cmd == BOT_FORWARD_ADJUST:
			print "BOT_FORWARD_ADJUST:", arg
			self.bot.forwardAdjust(arg)
		elif cmd == BOT_TRIM_LEFT:
			print "BOT_TRIM_LEFT:", arg
			self.bot.trimLeft(arg)
		elif cmd == BOT_TRIM_RIGHT:
			print "BOT_TRIM_RIGHT:", arg
			self.bot.trimRight(arg)

	def run(self):
		while True:
			cmd = self.getCommand()
			self.execute(cmd)