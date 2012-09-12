import time
import tuxcraft_tools
def command(thread):
	print 'Server list ping'
	thread.keepalivet.cancel()
	thread.channel.send( b'\xff' + tuxcraft_tools.minecraft_string(u'Tuxies Pythonserver\xa720\xa710') )
	time.sleep(5) # The procol docs state that this is necessery due to a bug in the client
	return -1
