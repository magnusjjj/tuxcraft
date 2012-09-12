# -*- coding: utf-8 -*-
import time
import struct
import tuxcraft_tools
def command(thread):
	print 'Close Window ' +	tuxcraft_tools.minecraft_read_byte(thread.channel) # Window id
