# -*- coding: utf-8 -*-
import time
import struct
import tuxcraft_tools
def command(thread):
#	print 'Player'
	thread.OnGround = tuxcraft_tools.minecraft_read_byte(thread.channel)
#	print thread.X, thread.Y, thread.Stance, thread.Z, thread.OnGround
