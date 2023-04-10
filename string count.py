str1=input('enter any string :')
def letter(str1):
    lower=0
    upper=0
    for i in str1:
        if(i.islower()):
            lower+=1
        else:
            upper+=1
    print("Upper case letter in given string =",upper)
    print("Lower case letter in given string =",lower)
letter(str1)
