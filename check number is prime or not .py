num=input('enter any number :')
def primeno(num):
    if(num==1):
        return False
    elif(num==2):
        return True
    else:
        for x in range(2,num):
            if(num%x==0):
                return False
            return True
        
