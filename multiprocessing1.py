import time

def DisplayEven(no):
    for i in range(no):
        if i % 2==0:
            print("Even no:",i)

def DisplayOdd(no):
    for i in range(no):
        if i % 2!=0:
            print("Odd no:",i)

def main():
    print("Demonstation of serial programming")
    DisplayEven(2000)
    DisplayOdd(2000)


if __name__=="__main__":
    start_time=time.process_time()
    main()
    end_time=time.process_time()

print("Execution time:",end_time-start_time)