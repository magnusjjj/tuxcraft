# -*- coding: utf-8 -*-
import time
import struct
import tuxcraft_tools
def command(thread):
	print 'Pluginmessage'
	channel = tuxcraft_tools.minecraft_read_string(thread.channel) # Message string
	length = tuxcraft_tools.minecraft_read_short(thread.channel) # Message string
	data = thread.channel.recv(length) # Message string
