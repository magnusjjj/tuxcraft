import time
import struct
import tuxcraft_tools
import zlib
import zlib
import math
from StringIO import StringIO
import nbt.nbt

class tuxcraft_chunker:
	def __init__(self):
		pass
		
	def trigger_move(self, thread):
		lastx = int(thread.lastX) >> 4
		lastz = int(thread.lastZ) >> 4
		currx = int(thread.X) >> 4
		currz = int(thread.Z) >> 4
		
		if lastx != currx or lastz != currz: # gone over a chunk boundary
			tosend = {}
			for x in range(currx - 7, currx + 7):
				for z in range(currz - 7, currz + 7):
					if x not in tosend:
						tosend[x] = {}
					tosend[x][z] = True
			for x in range(lastx - 7, lastx + 7):
				for z in range(lastz - 7, lastz + 7):
					try:
						del tosend[x][z]
					except:
						pass
					try:
						if len(tosend[x]) == 0:
							del tosend[x]
					except:
						pass
			for chunkx in tosend:
				for chunkz in tosend[chunkx]:
					self.send_chunk(thread, chunkx, chunkz) # TODO: Multichunk!
			thread.lastX = thread.X
			thread.lastZ = thread.Z
			return
	def send_chunk(self, thread, X, Z):
		return self.send_real_chunk(thread, X, Z)

	def send_real_chunk(self, thread, X, Z):
		regionfilename = "../tuxcraft_data/world/region/r." + str(int(math.floor(X/32))) + '.' + str(int(math.floor(Z/32))) + '.mca' 
		nbtfile = open(regionfilename, 'rb')
		try:
			localx = X % 32
			localz = Z % 32
			i = 32 * localz + localx
			header = nbtfile.read(4096)
			timestamps = nbtfile.read(4096)
			unpack = struct.unpack('>i', header[i*4:(i*4)+4])
			start = unpack[0] & 0xFF
			length =  unpack[0] >> 8
			nbtfile.seek(4096 * length)
			header_chunk = struct.unpack('>ib',nbtfile.read(5))
			content = nbtfile.read(header_chunk[0])
			decompressed =  zlib.decompress(content)
			mynbt = nbt.nbt.NBTFile(buffer=StringIO(decompressed))
			availablesections = 0
			biomes = str(mynbt["Level"]["Biomes"].value)
			chunkconcat = {}
			dataconcat = {}
			blocklightconcat = {}
			skylightconcat = {}
			
			for section in mynbt["Level"]["Sections"]:
				Y = section["Y"].value
				mask = 1 << Y
				availablesections = availablesections | mask
				chunkconcat[Y] = str(section["Blocks"].value)
				dataconcat[Y] = str(section["Data"].value)
				blocklightconcat[Y] = str(section["BlockLight"].value)
				skylightconcat[Y] = str(section["SkyLight"].value)

			tocompress = ""
			for i in range(16):
				if(i in chunkconcat):
					tocompress += chunkconcat[i]
			for i in range(16):
				if(i in chunkconcat):
					tocompress += dataconcat[i]
			for i in range(16):
				if(i in chunkconcat):
					tocompress += blocklightconcat[i]
			for i in range(16):
				if(i in chunkconcat):
					tocompress += skylightconcat[i]
			tocompress += biomes
			tocompress = zlib.compress(tocompress, 5)
			packet = b'\x33' + struct.pack('>iibHHi',X,Z,1,availablesections,0x0000,len(tocompress))+tocompress
			thread.send(packet)
		finally:
				nbtfile.close()

	def send_fake_chunk(self, thread, X, Z):
		compressme = b'\x07'*256 + '\x02' * 768 + b'\x00'*((4096*15)+(4096-1024)) # Fill bottom with air, the three lines over that with dirt, the rest air
		compressme += b'\x00'*(2048*16) # Meta
		compressme += b'\xFF'*(2048*16) # Block ligth
		compressme += b'\xFF'*(2048*16) # Sky light
		compressme += b'' # Add array
		compressme += b'\x01'*256 #Biome array (normal)
		compressme = zlib.compress(compressme, 1)
		packet = b'\x33' + struct.pack('>iibHHi',X,Z,1,0xFFFF,0x0000,len(compressme))+compressme
		thread.send(packet)