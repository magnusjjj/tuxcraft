# -*- coding: utf-8 -*-
import time
import struct
import tuxcraft_tools
import zlib

def send_fake_chunk(thread, X, Z):
	compressme = b'\x07'*256 + '\x02' * 768 + b'\x00'*((4096*15)+(4096-1024)) # Fill bottom with air, the three lines over that with dirt, the rest air
	compressme += b'\x00'*(2048*16) # Meta
	compressme += b'\xFF'*(2048*16) # Block ligth
	compressme += b'\xFF'*(2048*16) # Sky light
	compressme += b'' # Add array
	compressme += b'\x01'*256 #Biome array (normal)
	compressme = zlib.compress(compressme, 1)
	packet = b'\x33' + struct.pack('>iibHHi',X,Z,1,0xFFFF,0x0000,len(compressme))+compressme
	thread.channel.send(packet)

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
			send_fake_chunk(thread, x, z)
			x += 1
			if x == 8:
				x = -7
				z += 1 
			if z == 8:
				break
		thread.channel.send(struct.pack('>biii', 0x06, 0, 128, 0))
		thread.channel.send(struct.pack('>bddddffb', 0x0D, 0, 67.240000009536743, 128, 0, 0, 0, 1))
