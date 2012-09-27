# -*- coding: utf-8 -*-
import time
import struct
import tuxcraft_tools
def command(thread):
	print 'Tab completion '
	input = tuxcraft_tools.minecraft_read_string(thread.channel) # Message string
	thread.send(b'\xCB' + tuxcraft_tools.minecraft_string(input))
