import cv2
import os
import pytesseract
import json

import numpy as np

from pytesseract import Output
from pdf_to_image import convert_pdf_to_image
from seperate_pdf_pages import split_pdf
from crop_pdf import crop_pdf
from utilities import read_json

poppler_path = "C:\\Program Files\\poppler-0.68.0\\bin"

tesseract_cmd_path = "C:\\Users\\SEYKES\\AppData\\Local\\Programs\\Tesseract-OCR\\tesseract.exe"
pytesseract.pytesseract.tesseract_cmd = tesseract_cmd_path

path = os.getcwd()
path_of_image = os.path.join(path, "data\\first.pdf")


# split_pdf(path_of_image)

# data = read_json("config\pdf.json")

# file_details = data["files"]["fileDetails"]

# for file in file_details:
#     output_file_name = f"temp\\cropped_{file['name']}"
#     input_file_name = f"temp\\{file['name']}"
#     crop_pdf(input_file_name, output_file_name,
#              top=file["top"], bottom=file["bottom"], right=file["right"], left=file["left"])

# cropped_pdf_path = os.path.join(path, "temp\\cropped_Page_1.pdf")
# convert_pdf_to_image(cropped_pdf_path)

im = cv2.imread("temp/Page_1.png")
d = pytesseract.image_to_data(im, output_type=Output.DICT)
# print(d.keys())
data_word = {key: value for key, value in d.items() if key ==
             "top" or key == "text"}
# print(data_word)

zipped = list(zip(d["left"], d["text"], d["word_num"]))

# print(zipped)

# filter(zipped)
keys = []
values = []
for (left, text, word_number) in zipped:
    if left >= 430 and left <= 915:
        keys.append(text)
    elif left >= 1169 and left <= 3087:
        values.append(text)
    else:
        continue

# # print(keys)
# print(values)

keys_to_check = []
combined_text = []

for key in keys:
    if key != "":
        combined_text.append(key)
    elif len(combined_text) != 0:
        concatenated_text = " ".join(combined_text)
        keys_to_check.append(concatenated_text)
        combined_text.clear()
    else:
        continue
if len(combined_text) != 0:
    concatenated_text = " ".join(combined_text)
    keys_to_check.append(concatenated_text)

values_to_check = []
combined_text = []

for value in values:
    if value != "":
        combined_text.append(value)
    elif len(combined_text) != 0:
        concatenated_text = " ".join(combined_text)
        values_to_check.append(concatenated_text)
        combined_text.clear()
    else:
        continue
if len(combined_text) != 0:
    concatenated_text = " ".join(combined_text)
    values_to_check.append(concatenated_text)

items_to_be_removed = ["Calibrated item", "Remarks",
                       "Calibration", "Re-calibration due", "Certificate"]
for item in items_to_be_removed:
    keys_to_check.remove(item)

formatted_key_value_pairs = list(zip(keys_to_check, values_to_check))
# print(formatted_key_value_pairs)
json_output = json.dumps(dict(formatted_key_value_pairs))
print(json_output)
