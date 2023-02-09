def Square(no):
    return  (no * no)

def main():
    Data=[1,2,3,4,5]
    Result=[]

    for value in Data:
        Result.append(Square(value))
    print("Result of square:",Result)


if __name__=="__main__":
    main()