def Main():
    print("Enter no: ")
    No=int(input())

    print("factors are: ")

    i=1
    while (i< int(No/2)+1,1):
    #for i in range(1,int(No/2)+1,1):
        if No % i==0:
            print(i)
        i=i+1



if __name__=="__main__":
    Main()