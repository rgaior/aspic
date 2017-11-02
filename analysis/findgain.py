############################
## code to write the gain ##
## in np files            ##
############################
import numpy as np
import matplotlib.pyplot as plt
import sys
import os
import glob
cwd = os.getcwd()
#classpath = cwd + '/../classes/'
utilspath = cwd + '/../utils/'
sys.path.append(utilspath)
import utils
import constant

basefolder = constant.datafolder + '/gain/'


fgain1 = basefolder + 'gain1.txt'
[g1,gain1ch1,gain1ch2] = utils.readsimple(fgain1,3)
outname1 = 'gain1'

fgain2 = basefolder + 'gain2.txt'
[g2,gain2ch1] = utils.readsimple(fgain2,2)
outname2 = 'gain2'

fgain3 = basefolder + 'gain3.txt'
[g3,gain3ch1] = utils.readsimple(fgain3,2)
outname3 = 'gain3'

resfolder = constant.resultfolder + 'gain/'
np.savez(resfolder + outname1, gbin=g1, gain=gain1ch1)
np.savez(resfolder + outname2, gbin=g2, gain=gain2ch1)
np.savez(resfolder + outname3, gbin=g3, gain=gain3ch1)
#print 'rms = ' , 

