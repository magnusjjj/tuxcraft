# -*- coding: utf-8 -*-
import time
import struct
import tuxcraft_tools
def command(thread):
	#print 'Player Look'
	thread.Yaw = tuxcraft_tools.minecraft_read_float(thread.channel)
	thread.Pitch = tuxcraft_tools.minecraft_read_float(thread.channel)
	thread.OnGround = tuxcraft_tools.minecraft_read_byte(thread.channel)