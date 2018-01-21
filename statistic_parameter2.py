# -*- coding: utf-8 -*-
"""
Created on Sun Jan 21 23:14:00 2018

@author: yiyuezhuo
"""

from utils import take_current_image, fnt,image_list_to_video

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import ConnectionPatch

import scipy.stats as stats

from functools import reduce

    
class MultiDistribution(object):
    def __init__(self,expect):
        self.expect = expect
        self.norm = stats.norm(loc=expect,scale=1)
        self.norm_2 = stats.norm(loc=expect,scale=2)
        self.lognorm = stats.lognorm(np.sqrt(2*np.log(2)),loc = expect-2)
        self.chi2 = stats.chi2(expect)
        self.exp = stats.expon(scale=expect)
    def excited(self):
        print('excited!')

delta = 0.01

left = -1
right = 100
sample_size = 1000
#base_size = 6

graph_up = 1.0
graph_down = 0-delta
graph_left = -1
graph_right = 6

im_list = []

frame = 60
frame = 6

for expect in np.linspace(2,3,frame):
#for expect in [1,1.3,1.6,2]:
    print('expect:{} 2->3 60'.format(expect))
    len_axs = 5
    
    dis = MultiDistribution(expect)
    
    x = np.linspace(left,right,sample_size)
    step = x[1] - x[0]
    #step = 0.05
    #x = np.arange(left,right,step)
    
    fig, axs = plt.subplots(len_axs, 1, figsize=(8, 8))
    axs[0].plot(x,dis.norm.pdf(x))
    #axs[1].plot(x,norm_2.pdf(x))
    axs[1].plot(x,dis.lognorm.pdf(x))
    axs[2].plot(x,dis.chi2.pdf(x))
    axs[3].plot(x,dis.exp.pdf(x))
    
    pdf_list = [dis.norm.pdf(x)*step,
                dis.lognorm.pdf(x)*step,
                dis.chi2.pdf(x)*step,
                dis.exp.pdf(x)*step]
    sum_pdf = reduce(np.convolve, pdf_list)
    x2 = np.linspace(left*len(pdf_list),
                     right*len(pdf_list),
                     len(sum_pdf)) / len(pdf_list)
    axs[4].plot(x2,sum_pdf/step)
    
    coordsA = "data"
    coordsB = "data"
    con = ConnectionPatch(xyA=(expect,0.0), xyB=(expect, graph_up-delta  ), 
                          coordsA=coordsA, coordsB=coordsB,
                          axesA=axs[len_axs-1], axesB=axs[0], shrinkB=5)
    axs[len_axs-1].add_artist(con)
    
    for ax in axs:
        ax.set_xlim(graph_left,graph_right)
        ax.set_ylim(graph_down,graph_up)
        
    #ax.set_xlim(graph_left,graph_right)
    #ax.set_ylim(graph_down,graph_up*2)
    
    im_list.append(take_current_image())
    plt.clf()

image_list_to_video(im_list)
