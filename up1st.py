#This program is for corrcting the user's input by making the fisrt letter upwrote.
def up1(name):
    return name[0].upper()+name[1:].lower()

#Test the up1
c=map(up1,['jaSon','dicK','JohNson'])
for x in c:
    print x
