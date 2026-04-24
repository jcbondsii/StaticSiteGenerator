from page_generator import extract_title
import unittest

class TestExtractTitle(unittest.TestCase):
    def test_extract_title(self):
        markdown = "# This is a title\n\nThis is some content."
        self.assertEqual(extract_title(markdown), "This is a title")
        self.assertNotEqual(extract_title(markdown), "This is some content.")

    def test_no_heading(self):
        markdown = "This is some content without a heading."
        with self.assertRaises(ValueError):
            extract_title(markdown)
    def test_multiple_headings(self):
        markdown = "# Title 1\n\n## Title 2\n\nThis is some content."
        self.assertEqual(extract_title(markdown), "Title 1")

if __name__ == "__main__":
    unittest.main()