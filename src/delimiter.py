from textnode import TextNode, TextType
from htmlnode import HTMLNode

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