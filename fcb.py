class FCB:
    def __init__(self, name, size, start_block, created, modified):
        """
        Store metadata for a file.
        name: filename (string)
        size: file size in bytes
        start_block: where file begins on disk
        timestamps: created/modified times
        """
        pass

    def to_dict(self):
        """
        Convert FCB to dictionary format for saving to JSON.
        """
        pass

    def from_dict(data):
        """
        Convert a dictionary back into an FCB object.
        """
        pass
