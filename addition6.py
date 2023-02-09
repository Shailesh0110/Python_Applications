print("application to demonstation industrial programming")

def Addition(value1,value2):
    ans = value1 + value2
    return ans

def main():
    print("Enter first no:")
    no1=int(input())

    print("Enter second no:")
    no2=int(input())

    sum=Addition(no1,no2)

    print("addition is :",sum)

if __name__=="__main__":
    main()