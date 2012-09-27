# -*- coding: utf-8 -*-
import socket
import struct
import tuxcraft_tools
import tuxcraft_packets
import tuxcraft_tick
import time
import threading
from tuxcraft_chunker import tuxcraft_chunker


class TuxCraftThread(threading.Thread):
	def __init__(self, channel, details, ticker):
		threading.Thread.__init__(self)
		self.channel = channel
		self.details = details
		self.sent_chunks = 0
		self.ticker = ticker
		self.sendlock = threading.RLock()
		self.lastX = 0
		self.lastZ = 0
		self.X = 0
		self.Y = 0
		self.Z = 0
		self.chunker = tuxcraft_chunker()

	def send(self, string, blocking = True):
		self.sendlock.acquire()
		try:
			self.channel.send(string)
		finally:
			self.sendlock.release()

	def run(self):
		print 'New connection: ' , self.details
		while True:
			command = self.channel.recv( 1 )
			command = struct.unpack('B', command)[0]
			#print self.details, ' : ' , command
			if command in tuxcraft_packets.commands:
				response = tuxcraft_packets.commands[command](self)
				if response == -1:
					self.channel.close()
					break
			else:
				self.ticker.removeclient(self)
				print 'Sending kick!'
				self.channel.send( b'\xff' + tuxcraft_tools.minecraft_string(u'Unknown command: ' + unicode(command)) )
				time.sleep(5)
				self.channel.close()
				break

class TuxCraftServer:
	def run(self):
		self.BaseSocket = socket.socket (socket.AF_INET, socket.SOCK_STREAM)
		self.BaseSocket.bind( ('', 1337 ) )
		self.BaseSocket.listen ( 5 )
		
		self.ticker = tuxcraft_tick.TickThread()
		self.ticker.daemon = True
		self.ticker.start()
		
		while True:
			channel, details = self.BaseSocket.accept()
			thread = TuxCraftThread(channel, details, self.ticker)
			thread.daemon = True
			thread.start()
			#print thread
			self.ticker.addclient(thread)
if __name__ == "__main__":
	server = TuxCraftServer()
	server.run()

