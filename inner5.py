
def Sub(no1,no2):
    ans=0
    ans=no1-no2
    return ans

def Decorated_function(Function_Name):
    def inner(a,b):
        if a<b:
            a,b=b,a
        return Function_Name(a,b)
    return inner

def main():
    value1=int(input("Enter first no:"))
    value2 = int(input("Enter Second no:"))

    new_function=Decorated_function(Sub)
    print(new_function(value1,value2))

if __name__=="__main__":
    main()