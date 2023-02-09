def Fact(no):
    if no<=0:
        return 1
    else:
        return (no * Fact(no-1))

def main():
    ret=Fact(5)
    print("factorial is :",ret)

if __name__=="__main__":
    main()