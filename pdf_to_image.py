from pdf2image import convert_from_path
import os

poppler_path = "C:\\Program Files\\poppler-0.68.0\\bin"


def convert_pdf_to_image(path):
    
    pages = convert_from_path(path, 500, poppler_path=poppler_path)


    for page in pages:
        name = os.path.splitext(path)[0]
        image_name = f"{name}.png"
        page.save(image_name, "png")
    return image_name
        
    
