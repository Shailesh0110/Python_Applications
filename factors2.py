def Main():
    print("Enter no: ")
    No=int(input())

    print("factors are: ")
    for i in range(1,int(No/2)+1,1):
        if No % i==0:
            print(i)

if __name__=="__main__":
    Main()