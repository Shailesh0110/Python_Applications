class Value:
    def __init__(self,data):
        self.no=data

    def Sumfactor(self):
        sum=0
        for i in range(1,self.no):
             if self.no% i ==0:
                 sum=sum+i
        return sum

    def chkperfect(self):
        Ans= self.Sumfactor()
        if self.no==Ans:
            return True
        else:
            return False


    def chkprime(self):
        Ans = self.Sumfactor()
        if Ans==1:
            return True
        else:
            return False

def main():
    print("please enter no:")
    A= int(input())
    obj=Value(A)
    ret=obj.chkprime()
    if ret== True:
        print("{} is a prime no".format(A))
    else:
        print("{} is a not prime no".format(A))


if __name__=="__main__":
    main()