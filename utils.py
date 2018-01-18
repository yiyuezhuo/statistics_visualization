# -*- coding: utf-8 -*-
"""
Created on Thu Jan 18 08:15:27 2018

@author: yiyuezhuo
"""

import numpy as np
import matplotlib.pyplot as plt

import os
from PIL import Image,ImageDraw, ImageFont
import shutil


def take_current_image(code='RGB'):
    # It will not work in interactive command line since the
    # cache image will be displayed in command line and removed.
    canvas = plt.get_current_fig_manager().canvas
    canvas.draw()
    im = Image.frombytes(code, canvas.get_width_height(), 
                 canvas.tostring_rgb())
    return im

fnt = ImageFont.truetype(font='simsun.ttc', size=40)

def merge_images(cache_name = 'cache', pattern = '%010d.png', output_name = 'test.mp4'):
    arg = '{}/{}'.format(cache_name,pattern)
    os.system('ffmpeg -r 60 -f image2 -s 1920x1080 -i {} -vcodec libx264 -crf 25  -pix_fmt yuv420p {}'.format(arg,output_name))

def make_temp(cache_name):
    os.makedirs(cache_name, exist_ok=True)
    
def save_temp(cache_name, im_list, pattern='{:0>10}.png'):
    for i,im in enumerate(im_list):
        im.save('{}/{:0>10}.png'.format(cache_name,i))
        
def delete_temp(cache_name):
    shutil.rmtree(cache_name)
    
def image_list_to_video(im_list,cache_name='cache'):
    make_temp(cache_name)
    save_temp(cache_name,im_list)
    merge_images(cache_name)
    delete_temp(cache_name)
    


