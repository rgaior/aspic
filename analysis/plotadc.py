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

basefolder = constant.datafolder + '/20171019/bruit19_10/'
confolder = '/connectorandground/'
cablefolder = '/cableandground/'

gain = '1111'
#file = basefolder + confolder + '/DAMIC_2017_10_19_' + constant.corr20171019bruitconnect[gain] + '.txt'
#file = basefolder + cablefolder + '/DAMIC_2017_10_19_' + constant.corr20171019bruitcable[gain] + '.txt'
#file = constant.datafolder + '/20171020/meas1/' + '/DAMIC_2017_10_20' + '_165034.txt'
file = constant.datafolder + '/20171020/meas1/' + '/DAMIC_2017_10_20' + '_165545.txt'
file2 = basefolder + cablefolder + '/DAMIC_2017_10_19_' + constant.corr20171019bruitcable[gain] + '.txt'

[rep, adc1, adc2] = utils.readadcfile(file)
[rep2, adc1_2, adc2_2] = utils.readadcfile(file2)
print 'rms1 = ' , np.std(adc1)
print 'rms2 = ' , np.std(adc2)
figtrace = plt.figure()
plt.plot(rep,adc1-np.mean(adc1))
plt.plot(rep,adc2-np.mean(adc2))
plt.xlabel('time [a.u.]')
plt.ylabel('ADU')
plt.savefig(constant.plotfolder + '/adc1adc2.png')
figtracezoom = plt.figure()
plt.plot(rep,adc1-np.mean(adc1),'.-')
plt.plot(rep,adc2-np.mean(adc2),'.-')
plt.xlabel('time [a.u.]')
plt.ylabel('ADU')
plt.xlim(0,1000)
plt.savefig(constant.plotfolder + '/adc1adc2zoom2.png')
figcorrel = plt.figure()
plt.plot(adc1,adc2,'.')
plt.xlabel('ADU')
plt.ylabel('ADU')
plt.savefig(constant.plotfolder + '/adc1adc2correl.png')


#######FFT#######
figspec = plt.figure()
spec1 = np.absolute(np.fft.rfft(adc1-np.mean(adc1)))
spec2 = np.absolute(np.fft.rfft(adc1_2-np.mean(adc1_2)))
plt.semilogy(spec1)
plt.semilogy(spec2)



plt.show()
