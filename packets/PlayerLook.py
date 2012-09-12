# -*- coding: utf-8 -*-
import time
import struct
import tuxcraft_tools
def command(thread):
	print 'Player Look'
	thread.Yaw = tuxcraft_tools.minecraft_read_float(thread.channel)
	thread.Pitch = tuxcraft_tools.minecraft_read_float(thread.channel)
	thread.OnGround = tuxcraft_tools.minecraft_read_byte(thread.channel)
	print thread.Yaw, thread.Pitch, thread.OnGround
#	thread.channel.send(b'\x0D'+struct.pack('>ddddffb', thread.X, thread.Stance, thread.Y, thread.Z, thread.Yaw, thread.Pitch, thread.OnGround))
	#thread.channel.send(b'\x0D'+struct.pack('>ddddffb', thread.X, thread.Stance, thread.Y, thread.Z, thread.Yaw, thread.Pitch, thread.OnGround))
	#thread.channel.send( b'\xff' + tuxcraft_tools.minecraft_string(u'Du identifierade dig') )
	#time.sleep(5) # The procol docs state that this is necessery due to a bug in the client
	#thread.channel.send( b'\x01' + struct.pack('>i', 1238) + tuxcraft_tools.minecraft_string(u'default') + b'\x00\x00\x00\x00\x08' )
