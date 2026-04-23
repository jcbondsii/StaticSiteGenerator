import sys, os, shutil

def copy_folder(source, destination):
    if not os.path.exists(destination):
        os.makedirs(destination)
        
    for item in os.listdir(source):
        s = os.path.join(source, item)
        d = os.path.join(destination, item)
        if os.path.isdir(s):
            copy_folder(s, d)
            print(f"Copied folder: {s} to {d}")
        else:
            shutil.copy(s, d)
            print(f"Copied file: {s} to {d}")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python copy.py <source> <destination>")
        sys.exit(1)

    source = sys.argv[1]
    destination = sys.argv[2]

    if os.path.exists(destination):
        shutil.rmtree(destination)
    copy_folder(source, destination)
