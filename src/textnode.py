from htmlnode import LeafNode
from enum import Enum


class TextType(Enum):
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK= "link"
    IMAGE = "image"

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
    
    def text_node_to_html_node(text_node):
        if not isinstance(text_node.text_type, TextType):
            raise Exception("TYPE ERROR")
        match text_node.text_type:
            case TextType.TEXT:
                return LeafNode(None,text_node.text)
            case TextType.BOLD:
                return LeafNode("b",text_node.text)
            case TextType.ITALIC:
                return LeafNode("i",text_node.text)
            case TextType.CODE:
                return LeafNode("code",text_node.text)
            case TextType.LINK:
                return LeafNode("a",text_node.text,text_node.props)
            case TextType.IMAGE:
                return LeafNode("img","",text_node.props)
            case _:
                raise ValueError
    
    def split_nodes_delimiter(old_nodes, delimiter, text_type):
        for oldies in old_nodes:
            if oldies.text_type == TextType.TEXT:
                oldies.text.split(delimiter)
                