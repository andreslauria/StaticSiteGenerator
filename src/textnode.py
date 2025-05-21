from enum import Enum

class TextType(Enum):
    NORMAL = "normal text"
    BOLD = "**Bold text**"
    ITALIC = "_Italic text_"
    CODE = "`Code text`"
    LINKS = "[anchor text](url)"
    IMAGES = "![alt text](url)"

class TextNode:
    
    def __init__(self, TEXT,TEXT_TYPE,URL=None):
        self.text = TEXT
        self.text_type = TEXT_TYPE
        self.url = URL
    
    def __eq__(self, value):
        if (self.text == value.text) and (self.text_type == value.text_type) and (self.url == value.url):
            return True
    
    def __repr__(self):
        return f"TextNode({self.text},{self.text_type.value},{self.url})"