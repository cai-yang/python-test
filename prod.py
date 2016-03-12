#input a list, caculate the prod.
def mult(x,y):
    return x*y

def prod(a=None):
    if a==None:
        a=[]
        return 0
    return reduce(mult,a)
