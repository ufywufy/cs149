import json

FREE_LIST_PATH = "free_list.json"
free_list = []  # list of 0/1 values representing free/used blocks, since block size is 64, this list will be 1024/64 elements long

def initialize_free_list(total_blocks):
    """
    Create a new free list with all blocks free (0)
    """
    global free_list
    free_list = [0] * total_blocks
    save_free_list()

def load_free_list():
    """
    Load free_list.json into memory
    """
    global free_list
    try:
        with open(FREE_LIST_PATH, 'r') as file:
            free_list = json.load(file)
    except FileNotFoundError:
        free_list = []
    

def save_free_list():
    """
    Save free list back to free_list.json
    """
    with open(FREE_LIST_PATH, 'w') as file:
        json.dump(free_list, file)

def find_free_blocks(num_blocks):
    """
    Looks for the first contigous space of num_blocks free blocks (0) in free_list.
    Return a list of the indices of the free blocks found.

    Return None if not enough space
    """
    if num_blocks <= 0:
        return None
    
    free_block_indices = []
    for block in range(len(free_list)):
        if free_list[block] == 0:
            free_block_indices.append(block)
            if len(free_block_indices) == num_blocks:
                return free_block_indices
        else:
            free_block_indices = []
    
    if len(free_block_indices) < num_blocks:
        return None
    
    return free_block_indices

def allocate_blocks(block_indices):
    """
    Makes sure that block_indices_list is a list, then mark each referenced block
    as used (1) in free_list. 
    """
    if not isinstance(block_indices, list):
        block_indices = [block_indices]

    for block in block_indices:
        if 0 <= block < len(free_list):
            free_list[block] = 1
        else:
            raise IndexError("No block located at this index")
        
    save_free_list()    

    

def free_blocks(block_indices):
    """
   Makes sure that block_indices_list is a list, then mark each referenced block
    as free space (0) in free_list. 
    """
    if not isinstance(block_indices, list):
        block_indices = [block_indices]

    for block in block_indices:
        if 0 <= block < len(free_list):
            free_list[block] = 0
        else:
            raise IndexError("No block located at this index")
        
    save_free_list()

