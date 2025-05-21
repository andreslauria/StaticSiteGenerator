import unittest

from htmlnode import HTMLNode

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
    
if __name__ == "__main__":
    unittest.main()