import unittest
from htmlnode import HTMLNode

class TestHtmlNode(unittest.TestCase):
    def test_init(self):
        node = HTMLNode(tag="p", value="Hello, World!", children=[], props={})
        self.assertEqual(node.tag, "p")
        self.assertEqual(node.value, "Hello, World!")
        self.assertEqual(node.children, [])
        self.assertEqual(node.props, {})

    def test_props_to_html(self):
        node = HTMLNode(props={"class": "container", "id": "main"})
        self.assertEqual(node.props_to_html(), 'class="container" id="main"')

    def test_props_to_html_empty(self):
        node = HTMLNode(props={})
        self.assertEqual(node.props_to_html(), "")

    def test_repr(self):
        node = HTMLNode(tag='p', value='Hello, World!', children=[], props={'class': 'container'})
        self.assertEqual(repr(node), "HTMLNode(tag='p', value='Hello, World!', children=[], props={'class': 'container'})")