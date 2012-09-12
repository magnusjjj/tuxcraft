# -*- coding: utf-8 -*-
import time
import struct
import tuxcraft_tools
def command(thread):
	print 'Client Statuses'
	input = tuxcraft_tools.minecraft_read_byte() # Bitfield
