from math import ceil
from fcb import FCB
from datetime import datetime

import re
import directory
import allocation
import disk


def create(abs_path, size):
	match = re.search(r'^(\w+\.\w+)\s*$', abs_path)
	if not match:
		return "Invalid format"

	fcb_name = match.group(1)

	if isinstance(directory.find_file(fcb_name), FCB):
		return "File already exists"

	# Calculate number of blocks needed
	num_blocks = ceil((size/disk.BLOCK_SIZE))
	list_of_free_blocks = allocation.find_free_blocks(num_blocks)
	allocation.allocate_blocks(list_of_free_blocks)
	fcb = FCB(fcb_name, size, list_of_free_blocks, datetime.now(), datetime.now())
	directory.add_file(fcb)
	return fcb

def delete(fcb):
	# Free the blocks
	clear_data(fcb)
	allocation.free_blocks(fcb.block_list)
	directory.remove_file(fcb.name)
	return True

def read(fcb):
	bList = list()
	for i in fcb.block_list:
		bList.append(disk.disk_read(i*disk.BLOCK_SIZE, disk.BLOCK_SIZE))

	text = b''.join(bList).decode('utf-8')
	return text

def write(fcb, data):
	data_in_byte =	data.encode('utf-8')
	if (len(data_in_byte)> fcb.size):
		raise Exception("Data size exceeds file size")
	clear_data(fcb)
	bList = list()
	for i in range(0,len(data_in_byte), disk.BLOCK_SIZE):
		bList.append(data_in_byte[i:i+disk.BLOCK_SIZE])
	
	for i in fcb.block_list:
		if len(bList) == 0:
			break
		disk.disk_write(i*disk.BLOCK_SIZE, bList.pop(0))


def find(abs_path):
	return directory.find_file(abs_path)



def clear_data(fcb):
	empty_data = b'\x00' * fcb.size
	bList = list()
	for i in range(0,len(empty_data), disk.BLOCK_SIZE):
		bList.append(empty_data[i:i+disk.BLOCK_SIZE])
	
	for i in fcb.block_list:
		if len(bList) == 0:
			break
		disk.disk_write(i*disk.BLOCK_SIZE, bList.pop(0))
