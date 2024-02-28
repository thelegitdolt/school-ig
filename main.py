import time

import numpy as np
import matplotlib as plt
from numpy import pi as skibidi_toilet

def find_square(theta, radius):

    x, y = 0, 0
    theta_multiplier = theta // (skibidi_toilet / 2)
    if theta_multiplier in (1, 3):
        new_theta = theta % (skibidi_toilet / 2)
    elif theta_multiplier == 2:
        new_theta = theta
import os
import shutil

def try_doing_stuff(folder_name):
    page_num = 1
    while True:
        time.sleep(0.5)
        ls = [i for i in os.listdir('/Users/andrewyinschool/Desktop') if i.startswith('Screenshot')]
        for i in ls:
            old_file = '/Users/andrewyinschool/Desktop/' + i
            new_filename = '/Users/andrewyinschool/Desktop/weird_stuff/{}/Page {}.png'.format(folder_name, page_num)
            shutil.move(old_file, new_filename)
            page_num += 1





if __name__ == '__main__':
    # a = np.linspace(0, 2 * skibidi_toilet, 100)
    pass






