# TESting 

filenames = ['One:abc.txt','Two:newtowrk.pdf','Three:somimages.jpg']
for fname in filenames :
    fname = fname.replace(':','-',1)
    print(fname)

Tuples = (1,2,3,4,5,6)
print(Tuples)

filenames = ('One:abc.txt','Two:newtowrk.pdf','Three:somimages.jpg')
for fname in filenames :
    fname = fname.replace(':','-',1)
    print(fname)
    print(type(filenames))