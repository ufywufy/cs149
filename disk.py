PATH = "virtual.bin"
SIZE = 1024 * 1024
BLOCK_SIZE = 64

def initialize_disk():
    """
    Create virtual_disk.bin and fill it with zero bytes.
    Call this once at the beginning of the program.
    """
    pass

def disk_read(start_byte, length):
    """
    Read starting at start from virtual_disk.bin, stop reading at length
    """
    pass

def disk_write(start_byte, data):
    """
    Write raw bytes starting at start into virtual_disk.bin
    Overwrites existing content at those byte positions
    """
    pass