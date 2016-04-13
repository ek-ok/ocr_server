#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
This is the main part for OCR
"""

from PIL import Image, ImageFilter
import pytesseract
import requests
from StringIO import StringIO


def extract_text(url, sharpen=False):
    image_file = StringIO(requests.get(url).content)
    image = Image.open(image_file)

    if sharpen:
        image = image.filter(ImageFilter.SHARPEN)

    return pytesseract.image_to_string(image, lang='eng')
