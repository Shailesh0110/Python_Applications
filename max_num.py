
#application to findout the max number
def Maximum (value1,value2):
    if value1>value2:
        return value1
    else:
        return value2

def main():
    print("Enter first no:")
    no1 = int(input())

    print("Enter second no:")
    no2 = int(input())

    Ans=Maximum(no1,no2)

    print("Largest number is :", Ans)


if __name__ == "__main__":
    main()





