from copy import copy_folder
from page_generator import generate_page

def main():
    source = "./content/index.md"
    destination = "./public/index.html"
    template = "./template.html"
    generate_page(source, template, destination)

if __name__ == "__main__":
    main()
