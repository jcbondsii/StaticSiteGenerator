from textnode import *

def main():
    textB = TextNode("This is some bold text", TextType.BOLD)
    textI = TextNode("This is an italic text", TextType.ITALIC)
    textC = TextNode("This is some code text", TextType.CODE)
    textL = TextNode("This is some anchor text", TextType.LINK, url="https://www.boot.dev/")
    print(textB.__repr__())
    print(textI.__repr__())
    print(textC.__repr__())
    print(textL.__repr__())

if __name__ == "__main__":
    main()
