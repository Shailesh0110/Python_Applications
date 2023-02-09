print("application to demonstation industrial programming")

import marvallousmodule

def main():
    print("value of __name__ from main is:",__name__)
    print("Enter first no:")
    no1=int(input())

    print("Enter second no:")
    no2=int(input())

    sum=marvallousmodule.Addition(no1,no2)

    print("addition is :",sum)

if __name__=="__main__":
    main()