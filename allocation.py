FREE_LIST_PATH = "free_list.json"
free_list = []  # list of 0/1 values representing free/used blocks, since block size is 64, this list will be 1024/64 elements long

def initialize_free_list(total_blocks):
    """
    Create a new free list with all blocks free (0)
    """
    pass

def load_free_list():
    """
    Load free_list.json into memory
    """
    pass

def save_free_list():
    """
    Save free list back to free_list.json
    """
    pass

def find_free_blocks(num_blocks):
    """
    Scan free_list and return the starting index of the first
    available contiguous region of 'num_blocks' free blocks.

    Return None if not enough space
    """
    pass

def allocate_blocks(start_block, num_blocks):
    """
    Mark blocks in the range [start_block, start_block+num_blocks)
    as allocated (1)
    """
    pass

def free_blocks(start_block, num_blocks):
    """
    Mark blocks in that range as free (0)
    """
    pass
