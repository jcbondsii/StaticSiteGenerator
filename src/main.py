from copy import copy_folder

def main():
    source = "./static"
    destination = "./public"
    copy_folder(source, destination)

if __name__ == "__main__":
    main()
