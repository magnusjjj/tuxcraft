# -*- coding: utf-8 -*-
import time
import struct
import tuxcraft_tools
def command(thread):
	print 'Click Window'
	tuxcraft_tools.minecraft_read_byte(thread.channel) # Window id
	tuxcraft_tools.minecraft_read_short(thread.channel)  # Slot
	tuxcraft_tools.minecraft_read_byte(thread.channel) # Right-click
	tuxcraft_tools.minecraft_read_short(thread.channel)  # Action number
	tuxcraft_tools.minecraft_read_byte(thread.channel) # Shift
	tuxcraft_tools.minecraft_read_slot(thread.channel) # The item that was picked
