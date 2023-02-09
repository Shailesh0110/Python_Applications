def Demo1():
    print("inside Demo")

# fuction accept one parameter and return nothing
def Demo2(no):
    print("inside demo2 with argument:",no)

# function accept one parameter ans return one paramenter
def Demo3(no):
    print("inside demo3 with argmunt",no)
    return no+2

#fuction accept two parameter return one parameter
def Demo4(no1,no2):
    print("inside demo4")
    add=no1+no2
    return add

#fuction accept two parameter return two parameter
def Demo5(no1,no2):
    print("inside demo5")
    add = no1 + no2
    sub= no1-no2
    return add,sub


def Main():
    Demo1()
    Demo2(11)
    ans=Demo3(10)
    print("return vaue of demo3:",ans)
    ans = Demo4(10,11)
    print("return vaue of demo4:", ans)
    ans1,ans2 = Demo5(11, 10)
    print("return vaue of demo5:", ans1)
    print("return vaue of demo5:", ans2)

if __name__=="__main__":
    Main()


