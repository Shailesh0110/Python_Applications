
class Numbers:
    def __init__(self):
        self.size=0
        self.Arr= list()

    def Acccept(self):
        print("How many Elements you want to staore?")
        self.size=int(input())

        print("Please enter the elemnets")
        for i in range(0,self.size):
            value= int(input())
            self.Arr.append(value)

    def Display(self):
        print("elemnts from list are:")
        for i in range(0,self.size):
            print(self.Arr[i])



def main():
    obj=Numbers()
    obj.Acccept()
    obj.Display()

if __name__=="__main__":
    main()