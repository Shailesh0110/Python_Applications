


def Demo():
    print("inside Demo")

def Fun():
    print("inside fun")

def Hello(FPTR):
    print("inside hello")
    FPTR()

Hello(Demo)
print("**************")
Hello(Fun)
print("**************")
