import json

class FCB:
    def __init__(self, name, size, block_list, created, modified):
        """
        File Control Block (FCB) metadata for a file or directory.

        name:       filename (string)
        size:       file size in bytes
        block_list: list of disk blocks used by file
        created:    timestamp (string or datetime)
        modified:   timestamp
        """
        self.name = name
        self.size = size
        self.block_list = block_list
        self.created = created
        self.modified = modified

    def to_dict(self):
        """
        Convert FCB to dictionary format for saving to JSON.
        """
        return {
            "name": self.name,
            "size": self.size,
            "block_list": self.block_list,
            "created": self.created,
            "modified": self.modified,
        }


    @classmethod
    def from_dict(cls, data):
        return cls(
            name=data["name"],
            size=data["size"],
            block_list=data["block_list"],
            created=data["created"],      
            modified=data["modified"],
        )

