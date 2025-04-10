import os
import shutil
import re
import zipfile
import unicodedata

# Specify the particular note you want to process
note_name = 'Writeup.md'  # Replace with the name of the specific markdown file you want to process

# Paths to your Obsidian vault and Hugo export directory
obsidian_vault_path = 'I:\\Obsidian Vault\\Hackthebox - Titanic\\deliverables'  # Replace with the path to your Obsidian vault (Windows)
hugo_zip_output_path = 'C:\\Users\\'  # Path to where zip files should be saved (e.g., a temporary directory)
images_directory_path = 'I:\\Obsidian Vault\\Attachments'


# Function to process markdown file and move images
def process_markdown_file(md_file_path, post_folder):
    with open(md_file_path, 'r', encoding='utf-8') as md_file:
        content = md_file.read()

    # Find all image links (assuming they are relative to the markdown file)
    image_links = re.findall(r'!\[\[(.*?)\]\]', content)
    # Create the folder for the images in the page bundle
    images_folder = os.path.join(post_folder, 'images')
    os.makedirs(images_folder, exist_ok=True)
    # Loop through each image link, copy the image to the post folder, and update the markdown content
    for image_link in image_links:
        image_path = os.path.join(images_directory_path, image_link)
        
        if os.path.exists(image_path):
            # Copy the image to the post folder
            image_name = os.path.basename(image_path)
            sanitized_filename = unicodedata.normalize('NFKD', image_name).replace(' ', '_')
            shutil.copy(image_path, os.path.join(images_folder, sanitized_filename))
            
            # Update the image path in the markdown content
            new_markdown = f'![{image_name}](./images/{sanitized_filename})'
            content = content.replace(f'![[{image_link}]]', new_markdown)
        else:
            print(f"⚠️ Image not found: {image_path}")
    # Return the updated content
    return content

# Function to create the zip file
def create_zip_bundle(post_name, post_folder):
    # Path to the zip file
    zip_file_path = os.path.join(hugo_zip_output_path, f'{post_name}.zip')
    
    # Create a zip file of the post folder
    with zipfile.ZipFile(zip_file_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(post_folder):
            for file in files:
                file_path = os.path.join(root, file)
                # Add the file to the zip file, maintaining the folder structure inside the zip
                zipf.write(file_path, os.path.relpath(file_path, post_folder))

    print(f"Bundle for '{post_name}' zipped at {zip_file_path}")

# Function to copy markdown file to a temporary directory and process the images
def copy_markdown_file(md_file_path):
    # Get the base name of the post (this will be the folder and filename)
    post_name = os.path.basename(md_file_path).replace('.md', '')
    post_folder = os.path.join(hugo_zip_output_path, post_name)
    
    # Create the post folder in the temporary directory
    os.makedirs(post_folder, exist_ok=True)
    
    # Copy the Markdown file to the post folder
    destination_md_path = os.path.join(post_folder, 'index.md')
    shutil.copy(md_file_path, destination_md_path)
    
    # Process and update the markdown file with image paths
    updated_content = process_markdown_file(destination_md_path, post_folder)
    
    # Write the updated content back to the destination file
    with open(destination_md_path, 'w', encoding='utf-8') as md_file:
        md_file.write(updated_content)
    
    # Create a zip of the folder containing the Markdown file and images
    create_zip_bundle(post_name, post_folder)
    shutil.rmtree(post_folder)

# Main function to process the specific note
def main():
    # Construct the full path to the specific note you want to process
    note_path = os.path.join(obsidian_vault_path, note_name)
    
    # Check if the specified note exists
    if os.path.exists(note_path):
        print(f'Processing specific note: {note_path}')
        copy_markdown_file(note_path)
    else:
        print(f"Note '{note_name}' not found in the vault!")

if __name__ == '__main__':
    main()
