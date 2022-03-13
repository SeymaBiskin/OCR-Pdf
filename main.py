import cv2
import os
import pytesseract

import numpy as np

from pytesseract import Output
from pdf_to_image import convert_pdf_to_image

path = os.getcwd()
path_of_image = os.path.join(path, "data\\first.pdf")

convert_pdf_to_image(path_of_image)
