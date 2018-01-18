# -*- coding: utf-8 -*-
"""
Created on Thu Jan 18 08:12:24 2018

@author: yiyuezhuo
"""

from utils import take_current_image, fnt,image_list_to_video

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import ConnectionPatch

import scipy.stats as stats

    
class MultiDistribution(object):
    def __init__(self,expect):
        self.expect = expect
        self.norm_dis = stats.norm(loc=expect,scale=1)
        self.norm_2_dis = stats.norm(loc=expect,scale=2)
        self.lognorm_dis = stats.lognorm(np.sqrt(2*np.log(2)),loc = expect-2)
        self.chi2_dis = stats.chi2(expect)
        self.exp_dis = stats.expon(scale=expect)
    def excited(self):
        print('excited!')

delta = 0.01

left = -2
right = 5
up = 1.0
down = 0-delta
#base_size = 6


im_list = []

for expect in np.linspace(1,2,60):
#for expect in [1,1.3,1.6,2]:
    len_axs = 4
    
    dis = MultiDistribution(expect)
    x = np.linspace(left,right,100)
    
    fig, axs = plt.subplots(len_axs, 1, figsize=(6, 8))
    axs[0].plot(x,dis.norm_dis.pdf(x))
    #axs[1].plot(x,norm_2_dis.pdf(x))
    axs[1].plot(x,dis.lognorm_dis.pdf(x))
    axs[2].plot(x,dis.chi2_dis.pdf(x))
    axs[3].plot(x,dis.exp_dis.pdf(x))
    
    coordsA = "data"
    coordsB = "data"
    con = ConnectionPatch(xyA=(expect,0.0), xyB=(expect, up-delta  ), 
                          coordsA=coordsA, coordsB=coordsB,
                          axesA=axs[len_axs-1], axesB=axs[0], shrinkB=5)
    axs[len_axs-1].add_artist(con)
    
    for ax in axs:
        ax.set_xlim(-2,4)
        ax.set_ylim(-0.01,1)

    
    im_list.append(take_current_image())
    plt.clf()

image_list_to_video(im_list)
