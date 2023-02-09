
class Arthmetic:

    def __init__(self,A,B):
        print("Inside init method")
        self.No1= A
        self.No2= B

    def Addition(self):
        Ans=self.No1+self.No2
        return Ans

    def Substraction(self):
        Ans=self.No1-self.No2
        return Ans

def main():
    print("inside main method")

    obj=Arthmetic(11,10)
    output=obj.Addition()
    print("Addition is :",output)
    output = obj.Substraction()
    print("Substraction is :", output)

if __name__=="__main__":
    print("inside starter")
    main()