import time
import multiprocessing

def DisplayEven(no):
    for i in range(no):
        if i % 2==0:
            print("Even no:",i)

def DisplayOdd(no):
    for i in range(no):
        if i % 2!=0:
            print("Odd no:",i)

def main():
    print("Demonstation of parallel programming using multipleprocess")
    number=2000
    p1=multiprocessing.Process(target=DisplayEven,args=(number,))
    p2 =multiprocessing.Process(target=DisplayOdd, args=(number,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()
    print("End of main")

if __name__ == "__main__":
    start_time = time.process_time()
    main()
    end_time = time.process_time()
    print("Execution time is : ",end_time - start_time)