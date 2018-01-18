# -*- coding: utf-8 -*-
"""
Created on Thu Jan 18 08:15:15 2018

@author: yiyuezhuo
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import ConnectionPatch


def f(t):
    return np.exp(-t) * np.cos(2*np.pi*t)

t1 = np.arange(0.0, 5.0, 0.1)
t2 = np.arange(0.0, 5.0, 0.02)

plt.figure(1)
plt.subplot(211)
plt.plot(t1, f(t1), 'bo', t2, f(t2), 'k')

plt.subplot(212)
plt.plot(t2, np.cos(2*np.pi*t2), 'r--')

plt.stem(np.linspace(0.0,5.0,1), np.cos(np.linspace(0.0,5.0,1)), '-.')
plt.show()

import scipy.stats as stats


expect = 1

#x = np.linspace(0.1,4.0,100)

norm_dis = stats.norm(loc=expect,scale=1)
norm_2_dis = stats.norm(loc=expect,scale=2)
lognorm_dis = stats.lognorm(np.sqrt(2*np.log(2)),loc = expect-2)
chi2_dis = stats.chi2(expect)
exp_dis = stats.expon(scale=expect)

fig, axs = plt.subplots(5, 1, figsize=(6, 9))

x = np.linspace(-2,4.0,100)


axs[0].plot(x,norm_dis.pdf(x))
axs[1].plot(x,norm_2_dis.pdf(x))
axs[2].plot(x,lognorm_dis.pdf(x))
axs[3].plot(x,chi2_dis.pdf(x))
axs[4].plot(x,exp_dis.pdf(x))

xy = (1.0, 0.0)
coordsA = "data"
coordsB = "data"
con = ConnectionPatch(xyA=(1.0,0.0), xyB=(1.0,0.99  ), coordsA=coordsA, coordsB=coordsB,
                      axesA=axs[4], axesB=axs[0], shrinkB=5)
#ax1.add_artist(con)
axs[4].add_artist(con)

for ax in axs:
    ax.set_xlim(-2,4)
    ax.set_ylim(-0.01,1)

