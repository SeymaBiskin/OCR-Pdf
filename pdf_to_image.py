from pdf2image import convert_from_path
import os

poppler_path = "C:\\Program Files\\poppler-0.68.0\\bin"


def convert_pdf_to_image(path):
    
    pages = convert_from_path(path, 500, poppler_path=poppler_path)

    index = 1
    for page in pages:
        image_name = f"temp\Page_{index}.png"
        page.save(image_name, "png")
        index+=1
    
