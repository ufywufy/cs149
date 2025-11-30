import json
from tkinter import SE


class FCB:
    def __init__(self, name, size, start_block, created, modified, fType,abs_path):
        """
        Store metadata for a file.
        name: filename (string)
        size: file size in bytes
        start_block: where file begins on disk
        timestamps: created/modified times
        """
        self.name = name
        self.type = fType                   #txt, img, dir, etc.
        self.path = abs_path
        self.size = size
        self.start_block = start_block
        self.created = created
        self.modified = modified
        self.next_block = list()              # Pointer to next block in file chain
        pass

    def to_dict(self):
        """
        Convert FCB to dictionary format for saving to JSON.
        """
        return {
            "name": self.name,
            "type": self.type,
            "path": self.path,
            "size": self.size,
            "start_block": self.start_block,
            "created": self.created,
            "modified": self.modified,
            "next_block": self.next_block
        }


    def from_dict(cls,data):
        """
        Convert a dictionary back into an FCB object.
        """
        return cls(
            name=data["name"],
            type=data["type"],
            path=data["path"],
            size=data["size"],
            start_block=data["start_block"],
            created=data["created"],      
            modified=data["modified"],
            next_block=data["next_block"]
        )

