def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def main():
    print("Enter first no:")
    no1=int(input())

    print("Enter second no:")
    no2 = int(input())

    ans=add(no1,no2)
    print("addition is :",ans)

    ans = sub(no1, no2)
    print("Substraction is :", ans)


if __name__ == "__main__":
    main()