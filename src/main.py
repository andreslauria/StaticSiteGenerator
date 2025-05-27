import sys, os
from pathlib import Path
import shutil

from block_markdown import markdown_to_html_node
from htmlnode import HTMLNode

def copy_directory_recursive(src: Path, dst: Path):
   if not dst.exists():
      dst.mkdir()
   
   for file in src.iterdir():
      new_f = dst / file.name
      if file.is_dir():
            copy_directory_recursive(file, new_f)
      else:
            print(f"Copying {file} to {new_f}")
            shutil.copy(file, new_f)

def extract_title(markdown):
   for line in markdown.split('\n'):
      if line.startswith('# '):
         return line[2:].strip()
   raise Exception("No H1 title found in markdown")

def generate_page(from_path, template_path, dest_path, basepath):
   print(f"Generating page from {from_path} to {dest_path} using {template_path}")
   
   with open(from_path,'r') as f:
      markdown_content = f.read()
   
   with open(template_path,'r') as f:
      template_content = f.read()
   
   html_content = markdown_to_html_node(markdown_content).to_html()
   title = extract_title(markdown_content)
   
   full_html = template_content.replace('{{ Title }}', title).replace('{{ Content }}',html_content).replace('href="/', f'href="{basepath}').replace('src="/', f'src="{basepath}')
   
   os.makedirs(os.path.dirname(dest_path), exist_ok=True)
   
   with open(dest_path, 'w') as f:
      f.write(full_html)

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath):
   for root, _, files in os.walk(dir_path_content):
      for file in files:
         if file.endswith('.md'):
               from_path = os.path.join(root, file)
               relative_path = os.path.relpath(from_path, dir_path_content)
               dest_path = os.path.join(dest_dir_path, os.path.splitext(relative_path)[0] + '.html')
               generate_page(from_path, template_path, dest_path, basepath)




def main():
   if len(sys.argv) == 2:
      basepath = sys.argv[1]
   else:
      basepath = "/"

   print(basepath)
   project_root = Path(__file__).parent.parent

   dest_path = project_root / "docs"
   static_dir = project_root / "static"

   # remove before copying
   if dest_path.exists():
      shutil.rmtree(dest_path)

   copy_directory_recursive(static_dir, dest_path)

   from_path = project_root / "content"
   template_path = project_root / "template.html"

   generate_pages_recursive(from_path, template_path, dest_path, basepath)

   
   

main()
