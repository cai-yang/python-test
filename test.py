#This program is wrote just for testing the LANGUAGE CHOOSING function of ATOM
def my_printname(name,a=1):
    if a==1:
        print 'hello,%s'%(name)
        return 0
    elif a==0:
        print 'fuck you,%s'%(name)
        return 0
b=my_printname
namelist={1:'xiaoming',2:'azhe',3:'gongong'}
for key in namelist:
    b(namelist[key],key%2)
