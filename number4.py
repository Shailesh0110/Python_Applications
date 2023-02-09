class Numbers:
    def __init__(self):
        self.size = 0
        self.Arr = list()
        self.Acccept()

    def Acccept(self):
        print("How many Elements you want to store?")
        self.size = int(input())

        print("Please enter the elemnets")
        for i in range(0, self.size):
            value = int(input())
            self.Arr.append(value)

    def Display(self):
        print("elemnts from list are:")
        for i in range(0, self.size):
            print(self.Arr[i])

    def Summation(self):
        sum = 0
        for i in range(0, self.size):
            sum = sum + self.Arr[i]
        return sum

    def Avg(self):
        sum = 0
        for i in range(0, self.size):
            sum = sum + self.Arr[i]
        return sum / self.size

    def maximum(self):
        max = self.Arr[0]
        for i in range(0, self.size):
            if self.Arr[i]>max:
                max=self.Arr[i]
        return max

    def minimum(self):
        min = self.Arr[0]
        for i in range(0, self.size):
            if self.Arr[i]<min:
                min=self.Arr[i]
        return min


def main():
    obj = Numbers()
    #obj.Acccept()
    obj.Display()
    output = obj.Summation()
    print("Summation is :", output)
    output = obj.Avg()
    print("Avg is :", output)
    output = obj.maximum()
    print("max is :", output)
    output = obj.minimum()
    print("min is :", output)

if __name__ == "__main__":
    main()