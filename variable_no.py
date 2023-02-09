def add(*values):
    sum=0
    for no in values:
        sum= sum+no
    return sum

def add1(*values):
    sum=0
    '''for i in range(0,len(values),1):
        sum= sum+ values[i]'''
    for i in range(0,len(values),1):
        sum= sum+ values[i]

    return sum

def Main():
    ans=add(1,7,9,4,6,5)
    print("addition is:",ans)

    ans = add1(1, 7, 9, 4, 6, 5)
    print("addition is:", ans)


if __name__ == "__main__":
    Main()