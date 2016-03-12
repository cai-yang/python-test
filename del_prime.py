#delete the prime numbers in 1~100
def nopri(x):
    if x==1 or x==2 or x>100:
        return
    for a in range(2,x):
        if x % a == 0:
            return True
    return
filter(nopri,range(1,101))
