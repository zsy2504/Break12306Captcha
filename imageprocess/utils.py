import numpy as np
from PIL import Image

def minBoundingBox(img):
    matrix = np.array(img.convert("L"))
    matrix = np.where(matrix>200, 0, 1)
    col_hist = np.sum(matrix, 0)
    row_hist = np.sum(matrix, 1)
    left, right, top, bot = 0, len(col_hist)-1, 0, len(row_hist)-1
    while col_hist[left] == 0 and left < right: left += 1
    while col_hist[right] == 0 and left < right: right -= 1
    while row_hist[top] == 0 and top < bot: top += 1
    while row_hist[bot] == 0 and top < bot: bot -= 1
    img = img.crop((left, top, right, bot))
    return img

def resize(img):
    img = minBoundingBox(img)
    width, height = img.size
    new_height = 227 / width * height
    img = img.resize((227, new_height))
    result = Image.new('L', (227, 227), 255)
    result.paste(img, (0, (227 - new_height)//2))
    return result


def chopLabel(img):
    box = (118, 0, 218, 25)
    label = img.crop(box)

    label = resize(label)
    return label
