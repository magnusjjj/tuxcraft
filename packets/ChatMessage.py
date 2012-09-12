# -*- coding: utf-8 -*-
import time
import struct
import tuxcraft_tools
def command(thread):
	print 'Chat Message ' +	tuxcraft_tools.minecraft_read_string(thread.channel) # Message string
