import random

from PIL import Image


def generate_matrix(size: int = 10, amount_to_fill: int = 10):
    matrix = [[False] * size for _ in range(size)]
    while amount_to_fill > 0:
        x = random.randint(0, size - 1)
        y = random.randint(0, size - 1)
        if not matrix[x][y]:
            matrix[x][y] = matrix[x][size - y - 1] = True
            amount_to_fill -= 1

    return matrix


matrix = generate_matrix()
pixels = []
for row in matrix:
    pixels = pixels + row
conv_pixels = [1 if pixel else 0 for pixel in pixels]
img = Image.new('1', (len(matrix), len(matrix[0])))
img.putdata(conv_pixels)
resized = img.resize((1000, 1000), resample=Image.LANCZOS)
resized.save('black_white.png')
