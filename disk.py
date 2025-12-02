PATH = "virtual.bin"
SIZE = 1024 * 1024
BLOCK_SIZE = 64

def initialize_disk():
    """
    Create virtual_disk.bin and fill it with zero bytes.
    Call this once at the beginning of the program.
    """
    with open(PATH, "wb") as f:
        f.write(b'\x00' * SIZE)

def disk_read(start_byte, length):
    """
    Read starting at start from virtual_disk.bin, stop reading at length
    """
    with open(PATH, "rb") as f:
        f.seek(start_byte)
        return f.read(length)

def disk_write(start_byte, data):
    """
    Write raw bytes starting at start into virtual_disk.bin
    Overwrites existing content at those byte positions
    """
    with open(PATH, "r+b") as f:
        f.seek(start_byte)
        f.write(data)
