# -*- coding: utf-8 -*-
import struct

def minecraft_string(input_string):
	return struct.pack('>h',  len(input_string.encode('utf-16BE')) / 2) + input_string.encode('utf-16BE')

def minecraft_read_short(socket):
	return struct.unpack('>h', socket.recv(2))[0]

def minecraft_read_string(socket):
	input_string = socket.recv(minecraft_read_short(socket)*2)
	return input_string.decode('utf-16BE')

def minecraft_read_byte(socket):
	return struct.unpack('B', socket.recv(1))[0]

def minecraft_read_int(socket):
	return struct.unpack('>i', socket.recv(4))[0]

def minecraft_read_double(socket):
	return struct.unpack('>d', socket.recv(8))[0]

def minecraft_read_float(socket):
	return struct.unpack('>f', socket.recv(4))[0]

def minecraft_read_slot(socket):
	returner = []
	start = minecraft_read_short(socket)
	if start == -1:
		return returner
	
	else:
		item_count = minecraft_read_byte(socket)
		item_damage = minecraft_read_short(socket)
		item_meta_length = minecraft_read_short(socket)
		if item_meta_length != -1:
			socket.recv(item_meta_length)
	return returner
