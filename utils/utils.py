import numpy as np

def readadcfile(fname):
    f = open(fname,'r')
    lines = f.readlines()
    rep = np.array([])
    adc1 = np.array([])
    adc2 = np.array([])
    for l in lines[20:]:
        ls = l.split()
        rep = np.append(rep,int(ls[2]))
        adc1 = np.append(adc1,int(ls[3]))
        adc2 = np.append(adc2,int(ls[4]))
    return [rep, adc1, adc2]

def readsimple(fname,col):
    f = open(fname,'r')
    lines = f.readlines()
    if col > 3 :
        print 'doesn;t work with more than 3 column ! change the code it is simple'
        return 0
    c1 = np.array([])
    c2 = np.array([])
    c3 = np.array([])
    for l in lines[1:-1]:
        ls = l.split()
        print ls
        if col == 1:
#            c1 = np.append(c1,float(ls[0]))
            c1 = np.append(c1,ls[0])
        if col == 2:
            c1 = np.append(c1,ls[0])
            c2 = np.append(c2,float(ls[1]))
        if col == 3:
            c1 = np.append(c1,ls[0])
            c2 = np.append(c2,float(ls[1]))
            c3 = np.append(c3,float(ls[2]))
    if col == 1:
        return c1
    if col == 2:
        return [c1,c2]
    if col == 3:
        return [c1,c2,c3]



def chunks(l, n):
    """Yield successive n-sized chunks from l."""
    for i in range(0, len(l), n):
        yield l[i:i + n]


def sortgain(gainlist,gbinlist):
    a_out = np.array([])
    size = len(gainlist)
    afit = 0
    for i in range(size):
        if gainlist[i] == 'AF1':
            afit= i

    gaf1 = gainlist[afit]
    newgainlist = np.remove(gainlist,afit)
    newgainlistint = newgainlist.astype('int')
    newgainlistint.sort()
            
        
