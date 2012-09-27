# -*- coding: utf-8 -*-
import time
import struct
import tuxcraft_tools
def command(thread):
	print 'Player Block Placement'
	tuxcraft_tools.minecraft_read_int(thread.channel) # X
	tuxcraft_tools.minecraft_read_byte(thread.channel) # Y, Should be unsigned, but meh
	tuxcraft_tools.minecraft_read_int(thread.channel) # Z
	tuxcraft_tools.minecraft_read_byte(thread.channel) # Direction
	tuxcraft_tools.minecraft_read_slot(thread.channel) # Held item
	tuxcraft_tools.minecraft_read_byte(thread.channel) # Cursor X
	tuxcraft_tools.minecraft_read_byte(thread.channel) # Cursor Y
	tuxcraft_tools.minecraft_read_byte(thread.channel) # Cursor Z
