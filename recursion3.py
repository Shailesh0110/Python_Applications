
def Add(no):

    if no<=0:
        return 0
    else:
        return (no+Add(no-1))

def main():
    ret=Add(4)

    print("sumation is :",ret)


if __name__=="__main__":
    main()