
class HTMLNode:
    def __init__(self, tag=None,value=None,children=None,props=None):
        self.tag = tag
        self.value = value
        self.children =  children
        self.props = props
    
    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        if self.props is None:
            return ""
        result_string = props_to_string(self.props)
        return result_string
    
    def __repr__(self):
        return f"HTMLNode({self.tag},{self.value},{self.children},{self.props})"

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)
    
    def to_html(self):
        if self.value == None:
            raise ValueError
        if self.tag == None:
            return f"{self.value}"
        if self.props != None:
            result_string = props_to_string(self.props)
            return f"<{self.tag}{result_string}>{self.value}</{self.tag}>"
        
        return f"<{self.tag}>{self.value}</{self.tag}>"
    
class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)
 
    def to_html(self):
        if self.tag == None:
            raise ValueError("not tag")
        if self.children == None or self.children == []:
            raise ValueError("not childen")
        childs = ""
        for child in self.children:
              childs += child.to_html()  
        return f"<{self.tag}>{childs}</{self.tag}>"
 
 
 
    
def props_to_string(props):
    result_string = ""
    for key, value in props.items():
        result_string += f' {key}="{value}"'
    return result_string