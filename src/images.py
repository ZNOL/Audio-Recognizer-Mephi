import cv2
import pytesseract
import numpy as np
from matplotlib import pyplot as plt

# pytesseract.pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"   # STRING FOR WINDOWS


def image_processing(filePath):
    img = cv2.imread(filePath)
    img = img[0:540, 1520:1980]
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    config = r'--oem 3 --psm 6'
    data = pytesseract.image_to_data(img, config=config, lang="rus+eng")

    ans = ''
    prev = ''
    for i, el in enumerate(data.splitlines()):
        if i == 0:
            continue

        el = el.split()
        try:
            txt = el[11]
            if txt.isalpha():
                if txt == 'rosoput' or txt == 'говорит' or (txt.lower().count('o') != 1 and len(prev) >= 3):
                    ans = prev
                    break
                else:
                    if len(txt) <= 3:
                        prev = ''
                    else:
                        prev += ' ' + txt
        except IndexError:
            pass

    return ans
