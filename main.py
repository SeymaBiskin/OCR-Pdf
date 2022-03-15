import cv2
import os
import pytesseract
import json

import numpy as np

from pytesseract import Output
from pdf_to_image import convert_pdf_to_image
from seperate_pdf_pages import split_pdf
from crop_pdf import crop_pdf
from utilities import read_json, write_json
from combine_text_of_image_data import drop_spaces_from_text
from extract_key_value_pairs import extract_key_value_pair


poppler_path = "C:\\Program Files\\poppler-0.68.0\\bin"

tesseract_cmd_path = "C:\\Users\\SEYKES\\AppData\\Local\\Programs\\Tesseract-OCR\\tesseract.exe"
pytesseract.pytesseract.tesseract_cmd = tesseract_cmd_path

path = os.getcwd()
data = read_json("config\pdf.json")

for file in data["files"]:
    path_of_pdf = os.path.join(path, f"data\\{file}")
    split_pdf(path_of_pdf)
    file_details = data["files"][file]



for details in file_details:

    output_file_name = f"temp\\cropped_{details['name']}"
    input_file_name = f"temp\\{details['name']}"
    crop_pdf(input_file_name, output_file_name,
             top=details["top"], bottom=details["bottom"], right=details["right"], left=details["left"])

    cropped_image_path = convert_pdf_to_image(output_file_name)

    im = cv2.imread(cropped_image_path)
    d = pytesseract.image_to_data(im, output_type=Output.DICT)

    text_wit_left_coordinate_data = list(zip(d["left"], d["text"]))
    keys, values = extract_key_value_pair(text_wit_left_coordinate_data, details["keysCoordinate"], details["valuesCoordinate"])

    keys_to_check = drop_spaces_from_text(keys)
    values_to_check = drop_spaces_from_text(values)

    items_to_be_removed = details["keysToRemove"]
    for item in items_to_be_removed:
        keys_to_check.remove(item)
    
    formatted_key_value_pairs = list(zip(keys_to_check, values_to_check))

    write_json(formatted_key_value_pairs, details['name'])
  
 