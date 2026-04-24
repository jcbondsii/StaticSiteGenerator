from markdown_blocks import BlockType, block_to_block_type, markdown_to_blocks, markdown_to_html_node

def extract_title(markdown):
    blocks = markdown_to_blocks(markdown)
    for block in blocks:
        block_type = block_to_block_type(block)
        if block_type == BlockType.HEADING:
            return block[2:].strip()
    raise ValueError("No heading found in markdown")

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using template {template_path}")

    # Read the contents of the markdown file
    with open(from_path, 'r') as f:
        markdown_content = f.read()
    
    # Read the contents of the template file
    with open(template_path, 'r') as f:
        template_content = f.read()

    # convert markdown to html
    html_content = markdown_to_html_node(markdown_content)
    html_content = html_content.to_html()

    # grab the title from the markdown
    title = extract_title(markdown_content)

    # replace the title and content in the template
    template_content = template_content.replace("{{ Title }}", title)
    template_content = template_content.replace("{{ Content }}", html_content)

    # Write the generated HTML to the destination file
    with open(dest_path, 'w') as f:
        f.write(template_content)