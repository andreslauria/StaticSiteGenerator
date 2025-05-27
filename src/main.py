import sys
from pathlib import Path
import shutil

from block_markdown import markdown_to_html_node
from htmlnode import HTMLNode

def copy_directory_recursive(src, dst):
   if not dst.exists():
      dst.mkdir()
   
   for file in src.iterdir():
      new_f = dst / file.name
      if file.is_dir():
            copy_directory_recursive(f, new_f)
      else:
            print(f"Copying {f} to {new_f}")
            shutil.copy(file, new_f)


def main():
   pass
   
   
main()
