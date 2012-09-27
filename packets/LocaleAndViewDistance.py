0# -*- coding: utf-8 -*-
import time
import struct
import tuxcraft_tools
import zlib
import zlib
import math
from StringIO import StringIO
import nbt.nbt
from tuxcraft_chunker import tuxcraft_chunker



def command(thread):
	print 'Locale and View Distance'
	thread.Locale = tuxcraft_tools.minecraft_read_string(thread.channel)
	thread.ViewDistance = tuxcraft_tools.minecraft_read_byte(thread.channel)
	thread.ChatFlags = tuxcraft_tools.minecraft_read_byte(thread.channel)
	thread.Difficulty = tuxcraft_tools.minecraft_read_byte(thread.channel)
	
	print thread.Locale, thread.ViewDistance, thread.ChatFlags, thread.Difficulty
	if thread.sent_chunks == 0:
		thread.sent_chunks = 1
		x = -7
		z = -7
		while True:
			thread.chunker.send_chunk(thread, x, z)
			x += 1
			if x == 8:
				x = -7
				z += 1 
			if z == 8:
				break
		thread.send(struct.pack('>biii', 0x06, 0, 128, 0))
		thread.send(struct.pack('>bddddffb', 0x0D, 0, 67.240000009536743, 128, 0, 0, 0, 1))
