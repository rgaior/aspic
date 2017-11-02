import numpy as np
import matplotlib.pyplot as plt
import sys
import os
import glob
cwd = os.getcwd()
#classpath = cwd + '/../classes/'
utilspath = cwd + '/../utils/'
sys.path.append(utilspath)
#sys.path.append(classpath)
import utils
#import constant

basefolder = '/Users/gaior/DAMIC/data/elec/20171019/'

fgain1 = basefolder + 'gain1.txt'
[g1,gain1ch1,gain1ch2] = utils.readsimple(fgain1,3)

fgain2 = basefolder + 'gain2.txt'
[g2,gain2ch1] = utils.readsimple(fgain2,2)

fnoise1 = basefolder + 'noise1.txt'
[g3,noise1ch1,noise1ch2] = utils.readsimple(fnoise1,3)

fnoise2 = basefolder + 'noise2.txt'
[g4,noise2ch1,noise2ch2] = utils.readsimple(fnoise2,3)

#g1 = utils.converttobin(g1)
#g2 = utils.converttobin(g2)
#g3 = utils.converttobin(g3)
#g4 = utils.converttobin(g4)
#plt.plot(g1,gain1ch1,'o')
print g1
x = np.linspace(1,len(g1),len(g1))
x2 = np.linspace(1,len(g2),len(g2))
print len(x), ' ' , len(g1), ' ',  len(gain1ch1), ' ',  len(gain2ch1)
plt.xticks(x, g1, rotation='vertical')
plt.xticks(x2, g2, rotation='vertical')
#plt.plot(x,gain1ch1,'o',label='ch1')
#plt.plot(x,gain1ch2,'o',label='ch2')
#plt.plot(x,noise1ch1,'o',label='cable ch1')
#plt.plot(x,noise1ch2,'o',label='cable ch2')
plt.plot(x,noise2ch1,'o',label='connector ch1')
plt.plot(x,noise2ch2,'o',label='connector ch2')
#plt.plot(x2,gain2ch1,'x',label='after ~10 days')

#plt.ylabel('voltage gain')
plt.ylabel('Standard deviation [ADU]')
#plt.xlabel('gain setting')
plt.legend()
#plt.ylim(1,7)
plotfolder = '/Users/gaior/DAMIC/code/aspic/plots/'
#plt.savefig(plotfolder + '/noisecable.png')
plt.savefig(plotfolder + '/noiseconnector.png')
plt.show()
