# -*- coding: utf-8 -*-
import time
import struct
import tuxcraft_tools
def command(thread):
	print 'Player Digging'
	tuxcraft_tools.minecraft_read_byte(thread.channel) # Status
	tuxcraft_tools.minecraft_read_int(thread.channel)  # X
	tuxcraft_tools.minecraft_read_byte(thread.channel) # Y
	tuxcraft_tools.minecraft_read_int(thread.channel)  # Z
	tuxcraft_tools.minecraft_read_byte(thread.channel) # Face
