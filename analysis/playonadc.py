############################
## code to try things out ##
## like FFT or grouping   ##
## the bins etc           ##
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
#sys.path.append(classpath)
import utils
import constant

# check on the file /utils/constant.py that you put the right folder
basefolder = constant.datafolder + '/20171020/meas1/'

gain = '0000'
#file = basefolder + confolder + '/DAMIC_2017_10_19_' + constant.corr20171019bruitconnect[gain] + '.txt'
file = basefolder + '/DAMIC_2017_10_20_' + constant.g20171020meas1[gain] + '.txt'
#file = basefolder + cablefolder + '/DAMIC_2017_10_19_' + constant.corr20171019bruitcable[gain] + '.txt'

[rep, adc1, adc2] = utils.readadcfile(file)
print 'rms1 = ' , np.std(adc1)
print 'rms2 = ' , np.std(adc2)
adc1 = adc1[5:-3]
rep = rep[5:-3]
#adc1 = adc1[:len(adc1)/2]
#rep = rep[:len(rep)/2]
print 'len(adc1) = ', len(adc1) , 'len(rep) =  ', len(rep)
newadc = utils.chunks(adc1,6)
print adc1
adc1new = np.array([])
for i in newadc:
    adc1new = np.append(adc1new,np.mean(i))
print 'len(adc1new) = ' , len(adc1new)
repnew = np.linspace(0,len(adc1),len(adc1new)) + 9

#repnew = 6*repnew + 3*np.ones(len(adc1new))
#print repnew
fig = plt.figure(figsize=(12,6))
plt.plot(rep,adc1-np.mean(adc1),'.')
plt.plot(repnew,adc1new -np.mean(adc1new),'x-')
#plt.xlim(0,400)
#plt.savefig(constant.plotfolder + '/modeaf1_all.png')

##########FFT#######
figspec = plt.figure()
spec1 = np.absolute(np.fft.rfft(adc1new -np.mean(adc1new)))
dt = 1.3e-5
freq = np.fft.rfftfreq(len(adc1new),dt)
#spec2 = np.absolute(np.fft.rfft(adc1_2-np.mean(adc1_2)))
plt.semilogy(freq/1e3, spec1)
#plt.ylim(1)
#plt.ylabel('FFT spetrum [a.u.]')
#plt.xlabel('freq [kHz]')
#plt.savefig(constant.plotfolder + '/spec_AF1'+'.png')
 #plt.semilogy(spec2)




plt.show()
