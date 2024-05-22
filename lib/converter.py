import os
from PIL import Image

def convert_webp2pdf(directory_path, pdf_output_path):
    files = os.listdir(directory_path)

    images_to_pdf = []
    webp_files = [file for file in files if file.endswith('.webp')]

    webp_files.sort()
    
    for file in webp_files:
        webp_file_path = os.path.join(directory_path, file)
        image = Image.open(webp_file_path)
        images_to_pdf.append(image)
    
    if images_to_pdf:
        pdf_file_name = os.path.basename(directory_path) + '.pdf'
        pdf_file_path = os.path.join(pdf_output_path, pdf_file_name)
        
        images_to_pdf[0].save(pdf_file_path, save_all=True, append_images=images_to_pdf[1:])
        
        print(f"PDF created: {pdf_file_path}")

