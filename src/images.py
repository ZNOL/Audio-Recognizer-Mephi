import cv2
import numpy as np
from matplotlib import pyplot as plt
import pytesseract

# pytesseract.pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"


def image_processing(filePath):
    img = cv2.imread(filePath)
    img = img[0:540, 1520:1980]
    # print(img.shape)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    config = r'--oem 3 --psm 6'
    data = pytesseract.image_to_data(img, config=config, lang="rus+eng")
    data2 = pytesseract.image_to_data(img, output_type=pytesseract.Output.DICT, lang="rus+eng", config=config)

    # print(data)
    # print(' '.join(data2['text']))

    ans = ''
    prev = ''
    for i, el in enumerate(data.splitlines()):
        if i == 0:
            continue

        el = el.split()
        try:
            x, y, w, h = int(el[6]), int(el[7]), int(el[8]), int(el[9])
            cv2.rectangle(img, (x, y), (w + x, h + y), (0, 0, 255), 1)
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
                # print(f'Prev = {prev}')
                # print(el[11])
            # cv2.putText(img, el[11], (x, y), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 1)
        except IndexError:
            pass
            # print("Операция была пропущена")

    # cv2.imshow('Result', img)
    # cv2.waitKey(0)

    return ans
