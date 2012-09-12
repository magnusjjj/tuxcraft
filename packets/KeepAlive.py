# -*- coding: utf-8 -*-
import time
import struct
import tuxcraft_tools
def command(thread):
	print 'Keep Alive'
	thread.OnGround = tuxcraft_tools.minecraft_read_int(thread.channel)
	print thread.X, thread.Y, thread.Stance, thread.Z, thread.Yaw, thread.Pitch, thread.OnGround
	#thread.channel.send( b'\xff' + tuxcraft_tools.minecraft_string(u'Du identifierade dig') )
	#time.sleep(5) # The procol docs state that this is necessery due to a bug in the client
	#thread.channel.send( b'\x01' + struct.pack('>i', 1238) + tuxcraft_tools.minecraft_string(u'default') + b'\x00\x00\x00\x00\x08' )
