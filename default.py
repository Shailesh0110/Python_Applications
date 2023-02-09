
def area (radius,pi=3.14):
    result=pi*radius*radius
    return result

def Main():
    Rvalue=10.5
    Pvalue=3.14
    #positional
    ans=area(Rvalue,Pvalue)
    print("area of circle :",ans)
    print("***********************************")

    #keyword
    ans = area(radius=Rvalue, pi=Pvalue)
    print("area of circle :", ans)
    print("***********************************")

    # postional +defaut
    ans = area(10.5)
    print("area of circle :", ans)
    print("***********************************")

    #keyword
    ans = area(pi=7.10,radius=10.5)
    print("area of circle :", ans)
    print("***********************************")







if __name__ == "__main__":
    Main()
