import threading
import Queue
import time
import struct
import sys
import traceback

class TickThread(threading.Thread):
	def __init__(self):
		threading.Thread.__init__(self)
		self.clients = []
		self.commands = Queue.Queue()
		self.currtick = 0
		self.lastkeepalive = time.time()
	def addclient(self, client):
		self.clients.append(client)
	def removeclient(self, client):
		self.clients.remove(client)
	def run(self):
		while(True):
			time.sleep(0.05) # One tick
			currtick = time.time()*20
			
			for client in self.clients:
				try:
					client.send(struct.pack('>Bq', 4, currtick))
				except:
					print 'Removing client'
					self.removeclient(client)
					traceback.print_exc(file=sys.stdout)
			
			if 300 < (time.time() * 20 - self.lastkeepalive):
				print 'Keep alive'
				self.lastkeepalive = time.time()*20
				for client in self.clients:
					print "SENDING KEEP ALIVE"
					try:
						client.send('\x00\x00\x00\x00\x00') # send keep alive
					except:
						print 'Remove client in keep alive'
						self.removeclient(client)
						traceback.print_exc(file=sys.stdout)
		return
