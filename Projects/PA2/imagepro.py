import matplotlib.pyplot as plt
import numpy as np

def resize(img, scale):
    height = int(len(img) * scale)
    width = int(len(img[0]) * scale)
    new_image = np.zeros((height, width, 3), dtype=int)
    for row in range(height):
        for col in range(width):
            new_image[row, col] = img[int(row // scale), int(col // scale)]
    return new_image


def crop(img, region):
    x_min, y_min, x_max, y_max = region
    return img[x_min:x_max, y_min:y_max]


def blur(img, factor):
    new_img = pad(img, factor, factor)
    kernel_size = 2 * factor + 1
    newer_img = img.copy()
    for row in range(factor, new_img.shape[0] - factor):
        for col in range(factor, new_img.shape[1] - factor):
            values = new_img[row - factor:row + factor + 1, col - factor:col + factor + 1]
            value = np.sum(values) / (kernel_size ** 2)
            newer_img[row - factor, col - factor] = value

    return newer_img

def convolve(img, kernel, padding=1, strides=1):
    new_img = pad(img, padding, padding)
    newer_img = new_img.copy()

    for row in range(padding, new_img.shape[0] - padding, strides):
        for col in range(padding, new_img.shape[1] - padding):
            values = new_img[row - padding:row + padding + 1, col - padding:col + padding + 1]
            value = (values * kernel).sum()
            newer_img[row, col] = value
    return newer_img

def animate(img):
    raise NotImplementedError

def pad(img, xtra, y_tra):
    pad_img = np.zeros((img.shape[0] + (2 * xtra), img.shape[1] + (2 * y_tra)), dtype=int)
    pad_img[xtra:-xtra, y_tra:-y_tra] = img
    return pad_img

def generate_test_image(size):
    image = np.zeros((size, size, 3))
    for i in range(size):
        if i % 3 == 1:
            image[i, i] = [255, 0, 0]
        elif i % 3 == 2:
            image[i, i] = [0, 255, 0]
        else:
            image[i, i] = [0, 0, 255]
    return image
