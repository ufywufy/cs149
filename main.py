import directory
import allocation
import disk
import otherFunc
import os

def main():
    """
    CLI loop for simple file system.
    Commands:
        create <filename> <size>
        write <filename> "<data>"
        read <filename>
        search <filename>
        delete <filename>
        exit
    """
    initial() # initialize disk, free list, directory

    print_help()
    print("Type 'help' again to see available commands.\n")

    while True:
        command = input("FS> ").strip()

        if not command:
            continue  

        args = command.split(maxsplit=2)  
        cmd = args[0].lower()

        try:
            if cmd == "help":
                print_help()

            elif cmd == "create" and len(args) == 3:
                filename = args[1]
                size = int(args[2])
                otherFunc.create(filename, size)
                print(f"File '{filename}' created with size {size} bytes.")

            elif cmd == "write" and len(args) == 3:
                filename = args[1]
                data = args[2].strip('"')  # remove quotes
                fcb = otherFunc.find(filename)
                if fcb:
                    otherFunc.write(fcb, data)
                    print(f"Written to '{filename}': {data}")
                else:
                    print(f"File '{filename}' not found.")

            elif cmd == "read" and len(args) == 2:
                filename = args[1]
                fcb = otherFunc.find(filename)
                if fcb:
                    print(otherFunc.read(fcb))
                else:
                    print(f"File '{filename}' not found.")

            elif cmd == "search" and len(args) == 2:
                filename = args[1]
                fcb = otherFunc.find(filename)
                if fcb:
                    print(f"Found: {fcb}")
                else:
                    print(f"File '{filename}' not found.")

            elif cmd == "delete" and len(args) == 2:
                filename = args[1]
                fcb = otherFunc.find(filename)
                if fcb:
                    otherFunc.delete(fcb)
                    print(f"File '{filename}' deleted.")
                else:
                    print(f"File '{filename}' not found.")

            elif cmd == "exit":
                print("Exiting File System CLI.")
                break

            else:
                print("Invalid command. Type 'help' for a list of commands.")

        except Exception as e:
            print(f"Error: {e}")

    fs_exit()

def print_help():
    print("Available commands:")
    print("  create <filename> <size>")
    print("  write <filename> \"<data>\"")
    print("  read <filename>")
    print("  search <filename>")
    print("  delete <filename>")
    print("  exit")

def initial():
    if not os.path.exists(disk.PATH):
        disk.initialize_disk()

    if os.path.exists(allocation.FREE_LIST_PATH):
        allocation.load_free_list()
    else:
        allocation.initialize_free_list((int)(disk.SIZE/disk.BLOCK_SIZE))
    
    directory.load_directory()

def fs_exit():
    allocation.save_free_list()
    directory.save_directory()


def reset():
    disk.initialize_disk()
    allocation.initialize_free_list((int)(disk.SIZE/disk.BLOCK_SIZE))
    directory.initial_directory()


if __name__ == "__main__":
    main()
