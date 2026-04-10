from enum import Enum

class TextType(Enum):
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"

class TextNode:
    def __init__(self, text: str, text_type: TextType, url: str = None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def render(self) -> str:
        if self.text_type == TextType.BOLD:
            return f"**{self.text}**"
        elif self.text_type == TextType.ITALIC:
            return f"_{self.text}_"
        elif self.text_type == TextType.CODE:
            return f"`{self.text}`"
        elif self.text_type == TextType.LINK:
            return f"[{self.text}]({self.url})"
        elif self.text_type == TextType.IMAGE:
            return f"![{self.text}]({self.url})"
        else:
            return self.text
    
    def __eq__(self, value):
        if not isinstance(value, TextNode):
            return False
        return self.text == value.text and self.text_type == value.text_type and self.url == value.url
    
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"