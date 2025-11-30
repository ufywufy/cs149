from tkinter.filedialog import Directory
from fcb import FCB
from datetime import datetime
from directory import *

import re
import disk
import allocation


def Create(abs_path, size):
	match = re.search(r'^(.*\\)(\w+)\.(\w+)\s*$', abs_path)
	if not match:
		return "Invalid format"

	fcb_name = match.group(2)
	fcb_fType = match.group(3)
	# Calculate number of blocks needed
	num_blocks = (size/disk.BLOCK_SIZE)+1
	list_of_free_blocks = allocation.find_free_blocks(num_blocks)
	fcb = FCB(fcb_name, size, list_of_free_blocks, datetime.now(), datetime.now(), fcb_fType,abs_path)
	directory.add_file(fcb)

	return fcb

def Delete(fcb):
	# Free the blocks
	allocation.free_blocks(fcb.block_list)
	directory.remove_file(fcb.name)
	return True

def Read(fcb):

	pass

def Write(fcb, data, offset):
	pass