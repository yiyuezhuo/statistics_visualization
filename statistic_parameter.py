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

left = -1
right = 1000
sample_size = 1000
#base_size = 6

graph_up = 1.0
graph_down = 0-delta
graph_left = -1
graph_right = 6

im_list = []

for expect in np.linspace(2,3,60):
#for expect in [1,1.3,1.6,2]:
    len_axs = 4
    
    dis = MultiDistribution(expect)
    
    x = np.linspace(left,right,sample_size)
    #step = 0.05
    #x = np.arange(left,right,step)
    
    fig, axs = plt.subplots(len_axs, 1, figsize=(6, 8))
    axs[0].plot(x,dis.norm_dis.pdf(x))
    #axs[1].plot(x,norm_2_dis.pdf(x))
    axs[1].plot(x,dis.lognorm_dis.pdf(x))
    axs[2].plot(x,dis.chi2_dis.pdf(x))
    axs[3].plot(x,dis.exp_dis.pdf(x))
    
    coordsA = "data"
    coordsB = "data"
    con = ConnectionPatch(xyA=(expect,0.0), xyB=(expect, graph_up-delta  ), 
                          coordsA=coordsA, coordsB=coordsB,
                          axesA=axs[len_axs-1], axesB=axs[0], shrinkB=5)
    axs[len_axs-1].add_artist(con)
    
    for ax in axs:
        ax.set_xlim(graph_left,graph_right)
        ax.set_ylim(graph_down,graph_up)

    
    im_list.append(take_current_image())
    plt.clf()

image_list_to_video(im_list)
