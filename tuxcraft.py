# -*- coding: utf-8 -*-
import socket
import struct
import tuxcraft_tools
import tuxcraft_packets
import time
import threading

class TuxCraftThread(threading.Thread):
	def __init__(self, channel, details):
		threading.Thread.__init__(self)
		self.channel = channel
		self.details = details
		self.sent_chunks = 0

	def keepalive(self):
		self.channel.send('\x00\x00\x00\x00\x00') # send keep alive
		self.keepalivet = threading.Timer(10.0, TuxCraftThread.keepalive, (self,))
		self.keepalivet.start()
	
	def run(self):
		print 'New connection: ' , self.details
		print 'Starting keep alive thread'
		self.keepalivet = threading.Timer(10.0, TuxCraftThread.keepalive, (self,))
		self.keepalivet.start()
		while True:
			command = self.channel.recv( 1 )
			command = struct.unpack('B', command)[0]
			print self.details, ' : ' , command
			if command in tuxcraft_packets.commands:
				response = tuxcraft_packets.commands[command](self)
				if response == -1:
					self.channel.close()
					break
			else:
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

		while True:
			channel, details = self.BaseSocket.accept()
			thread = TuxCraftThread(channel, details)
			thread.start()

if __name__ == "__main__":
	server = TuxCraftServer()
	server.run()

