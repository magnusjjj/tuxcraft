# -*- coding: utf-8 -*-
import time
import struct
import tuxcraft_tools
def command(thread):
	print 'Animation'
	tuxcraft_tools.minecraft_read_int(thread.channel)
	thread.Animation = tuxcraft_tools.minecraft_read_byte(thread.channel)
	print thread.Animation
