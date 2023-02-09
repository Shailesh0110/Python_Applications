def checkEven(no):
    if no%2==0:
        return True
    else:
        return False

def checkEven1(no):
    return no %2 ==0

Ret=checkEven1(12)

if Ret==True:
    print("even")
else:
    print("odd")