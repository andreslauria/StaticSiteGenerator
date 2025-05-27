from markdown_utils import extract_markdown_images, extract_markdown_links
from block_markdown import markdown_to_blocks
import block_markdown
import unittest


class TestExtractionMarkdown(unittest.TestCase):
    
    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)
        
    def test_extract_markdown_links(self):
        matches = extract_markdown_links(
            "This is text with a link [boot](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        )
        self.assertListEqual([("boot","https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")], matches)
        
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )


def test_three_blocks(self):
        markdown = """
# This is a heading

This is a paragraph of text. It has some **bold** and _italic_ words inside of it.

* This is a list item
* This is another list item
"""

        result = markdown_to_blocks(markdown)

        expected_result = [
            "# This is a heading",
            "This is a paragraph of text. It has some **bold** and _italic_ words inside of it.",
            "* This is a list item\n* This is another list item",
        ]

        self.assertListEqual(result, expected_result)


def test_three_blocks_extra_lines(self):
        markdown = """
# This is a heading





This is a paragraph of text. It has some **bold** and _italic_ words inside of it.





* This is a list item
* This is another list item
"""

        result = markdown_to_blocks(markdown)

        expected_result = [
            "# This is a heading",
            "This is a paragraph of text. It has some **bold** and _italic_ words inside of it.",
            "* This is a list item\n* This is another list item",
        ]

        self.assertListEqual(result, expected_result)

def test_three_blocks_group(self):
    markdown = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

* This is a list
* with items
"""

    result = markdown_to_blocks(markdown)

    expected_result = [
            "This is **bolded** paragraph",
            "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
            "* This is a list\n* with items",
        ]

    self.assertListEqual(result, expected_result)


class TestBlockToBlockType(unittest.TestCase):
    def test_h1(self):
        markdown_block = "# This is a h1 heading"

        result = block_markdown.block_to_block_type(markdown_block)

        expected_result = block_markdown.BlockType.HEADING

        self.assertEqual(result, expected_result)

    def test_h6(self):
        markdown_block = "###### This is a h6 heading"

        result = block_markdown.block_to_block_type(markdown_block)

        expected_result = block_markdown.BlockType.HEADING

        self.assertEqual(result, expected_result)
        
    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""

        node = block_markdown.markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )


        
if __name__ == "__main__":
    unittest.main()
