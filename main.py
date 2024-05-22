import os
import shutil
from lib.zip import open_and_deletezip
from lib.converter import convert_webp2pdf

def main():
    root_dir = os.path.dirname(__file__)
    converter_dir = os.path.join(root_dir, 'converter')
    pdf_dir = os.path.join(root_dir, 'pdf')
    
    # step1: decompress zip file
    open_and_deletezip(converter_dir)

    # step2: convert image to pdf
    for subdir in os.listdir(converter_dir):
        subdir_path = os.path.join(converter_dir, subdir)
        if os.path.isdir(subdir_path):
            convert_webp2pdf(subdir_path, pdf_dir)
            shutil.rmtree(subdir_path)

if __name__ == '__main__':
    main()
