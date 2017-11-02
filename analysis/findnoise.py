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
import constant

basefolder = constant.datafolder + '/20171020/meas1/'
a_rms = np.array([])
a_gain = np.array([])
for gbin,gfile in constant.g20171020meas1.items():
    file = basefolder + '/DAMIC_2017_10_20_' + gfile + '.txt'
    print file
    [rep, adc1, adc2] = utils.readadcfile(file)
    print 'rms1 = ' , np.std(adc1)
    print 'rms2 = ' , np.std(adc2)
    adc1 = adc1[5:-3]
    rep = rep[5:-3]
    newadc = utils.chunks(adc1,6)
    adc1new = np.array([])
    for i in newadc:
        adc1new = np.append(adc1new,np.mean(i))
    repnew = np.linspace(0,len(adc1),len(adc1new)) + 9

    rms = np.std(adc1new)
    print rms
    a_rms = np.append(a_rms, rms)
    a_gain = np.append(a_gain,gbin)

resfolder = constant.resultfolder + 'musigma/'
outname = 'meas1'
np.savez(resfolder + outname, gbin=a_gain, rms= a_rms)
#print 'rms = ' , 

