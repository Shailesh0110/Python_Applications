# OBJECT ORIENTED PROGRAMMING
# class= characterstics+ behavior
#class= data + functions

# accept 2 no and perform addition and substraction of it

# kai karaiche  ---> add & sub ---> no1 & no2 ---> characterstics

# kas karanr ahot ----> accept 2 nos ---> behavior (method/function)

class Arithematic:
    def __init__(self,a,b):
        self.no1=a
        self.no2=b

    def Add(self):
        return self.no1+self.no2

    def Sub(self):
        return self.no1-self.no2

def main():
    print("Enter first no:")
    value1=int(input())

    print("Enter second no:")
    value2= int(input())

    obj= Arithematic(value1,value2)

    ans=obj.Add()
    print("Addition is:",ans)

    ans = obj.Sub()
    print("Substraction is:", ans)



if __name__ == "__main__":
    main()