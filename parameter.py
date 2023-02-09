# positional argument/keyword argument
def add1(no1, no2):
    print("value of :", no1)
    print("value of :", no2)
    return no1 + no2


def sub1(no1, no2):
    print("value of :", no1)
    print("value of :", no2)
    return no1 - no2


#
def Main():
    ans = 0
    ans = add1(10, 11)
    print("addition is :", ans)

    ans = sub1(no1=20, no2=30)
    print("subtractions is :", ans)


if __name__ == "__main__":
    Main()
