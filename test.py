# -*- coding: utf-8 -*-
"""
Created on Sat Dec 30 22:25:47 2017

@author: yiyuezhuo
"""

import numpy as np
import matplotlib.pyplot as plt

import os
from PIL import Image,ImageDraw, ImageFont


def take_current_image(code='RGB'):
    # It will not work in interactive command line since the
    # cache image will be displayed in command line and removed.
    canvas = plt.get_current_fig_manager().canvas
    canvas.draw()
    im = Image.frombytes(code, canvas.get_width_height(), 
                 canvas.tostring_rgb())
    return im


tl = np.linspace(0.5,1,60)

x = np.linspace(0,10,100)

os.makedirs('cache',exist_ok=True)

func_im_list = []

for i,t in enumerate(tl):
    y = t*np.sin(x)
    name = '{0:0>10}.png'.format(i)
    path = 'cache/'+ name
    
    #plt.figure()
    plt.plot(x,y)
    plt.ylim(-1.1,1.1)
    #plt.savefig(path)
    func_im_list.append(take_current_image())
    plt.clf()
    print('func_im_list {}'.format(i))

im_list = []
fnt = ImageFont.truetype(font='simsun.ttc', size=40)


for i,func_im in enumerate(func_im_list):
    im = Image.new('RGB',(540,420),'white')
    m_shift,n_shift = 10,10
    box = (m_shift, n_shift, m_shift+func_im.size[0], n_shift+func_im.size[1])
    im.paste(func_im,box)
    d = ImageDraw.Draw(im)
    text = str(i)
    xy = (m_shift*2+func_im.size[0], n_shift*2+func_im.size[1])
    d.text(xy,text,font=fnt,fill=(255,0,0))
    im_list.append(im)
    print('im_list {}'.format(i))

for i,im in enumerate(im_list):
    im.save('cache2/{:0>10}.png'.format(i))