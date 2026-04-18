from textnode import TextNode, TextType, LeafNode
from htmlnode import HTMLNode
import re

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type == TextType.TEXT:
            split_values = node.text.split(delimiter)
            if len(split_values) % 2 == 0:
                raise ValueError(f"Invalid text node: unbalanced delimiter {delimiter} in text: {node.text}")            
            for i, value in enumerate(split_values):
                if value == "":
                    continue
                if i%2 == 0:
                    new_nodes.append(TextNode(value, TextType.TEXT))
                else:
                    new_nodes.append(TextNode(value, text_type))
        else:
            new_nodes.append(node)
    return new_nodes

def extract_markdown_images(text):
    pattern = r"!\[([^\[\]]*)\]\(([^\(\)]*)\)"
    matches = re.findall(pattern, text)
    return matches


def extract_markdown_links(text):
    pattern = r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)"
    matches = re.findall(pattern, text)
    return matches

def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        images = extract_markdown_images(node.text)
        if not images:
            new_nodes.append(node)
            continue
        
        remaining = node.text
        for image_alt, image_link in images:
                image_markdown = f"![{image_alt}]({image_link})"
                sections = remaining.split(image_markdown, 1)
                if sections[0] != "":
                    new_nodes.append(TextNode(sections[0], TextType.TEXT))
                new_nodes.append(TextNode(image_alt, TextType.IMAGE, image_link))
                remaining = sections[1]
        if remaining != "":
            new_nodes.append(TextNode(remaining, TextType.TEXT))
    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        links = extract_markdown_links(node.text)
        if not links:
            new_nodes.append(node)
            continue
        
        remaining = node.text
        for link_text, url in links:
                link_markdown = f"[{link_text}]({url})"
                sections = remaining.split(link_markdown, 1)
                if sections[0] != "":
                    new_nodes.append(TextNode(sections[0], TextType.TEXT))
                new_nodes.append(TextNode(link_text, TextType.LINK, url))
                remaining = sections[1]
        if remaining != "":
            new_nodes.append(TextNode(remaining, TextType.TEXT))
    return new_nodes