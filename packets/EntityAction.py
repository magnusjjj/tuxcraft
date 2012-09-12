# -*- coding: utf-8 -*-
import time
import struct
import tuxcraft_tools
def command(thread):
	#print 'Entity Action'
	tuxcraft_tools.minecraft_read_int(thread.channel) #EID
	tuxcraft_tools.minecraft_read_byte(thread.channel) #Action ID
