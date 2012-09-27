# -*- coding: utf-8 -*-
import time
import struct
import tuxcraft_tools
def command(thread):
	print 'Handshake'
	thread.ProtocolVersion = tuxcraft_tools.minecraft_read_byte(thread.channel)

	thread.Username = tuxcraft_tools.minecraft_read_string(thread.channel)
	thread.ServerHost = tuxcraft_tools.minecraft_read_string(thread.channel)
	thread.ServerPort = tuxcraft_tools.minecraft_read_int(thread.channel)
	print thread.ProtocolVersion, thread.Username, thread.ServerHost, thread.ServerPort
	#thread.channel.send( b'\xff' + tuxcraft_tools.minecraft_string(u'Du identifierade dig') )
	#time.sleep(5) # The procol docs state that this is necessery due to a bug in the client
	thread.send( b'\x01' + struct.pack('>i', 1238) + tuxcraft_tools.minecraft_string(u'default') + b'\x00\x00\x00\x00\x08' )
