import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_not_eq(self):
        node = TextNode("This is a text node", TextType.ITALIC)
        node2 = TextNode("This is also a text node", TextType.TEXT)
        self.assertNotEqual(node, node2)

    def test_no_url(self):
        node = TextNode("This text node has no URL", TextType.TEXT)
        return node.url is None
    
    def test_is_url(self):
        node = TextNode("This text node has a URL", TextType.TEXT, "https://wwww.textnode.com")
        return node.url is not None

if __name__ == "__main__":
    unittest.main()