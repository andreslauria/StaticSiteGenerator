import unittest

from htmlnode import HTMLNode,LeafNode,ParentNode

class TestHtmlNode(unittest.TestCase):
    def testPropsToHtml(self):
        node = HTMLNode("a", "clikeame", None, {"href": "https://ldldl", "target": "_blank"})
        expected = ' href="https://ldldl" target="_blank"'
        self.assertEqual(node.props_to_html(), expected)
    
    def testEmptyProps(self):
        node = HTMLNode("p", "Hello", None, None)
        self.assertEqual(node.props_to_html(), "")
    
    def testRepr(self):
        node = HTMLNode("div", "content", None, {"class": "container"})
        expected = "HTMLNode(div,content,None,{'class': 'container'})"
        self.assertEqual(repr(node), expected)
    
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
        
        
    def test_leaf_to_html_p(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), '<a href="https://www.google.com">Click me!</a>')
        
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
            )
    
if __name__ == "__main__":
    unittest.main()