import os
import multiprocessing0

def Square(no):
    print("PID of worker processis {} for the input{}".format(os.getpid(),no))
    return  (no * no)

def main():
    print("Process ID of ous application is :",os.getpid())
    Data=[1,2,3,4,5]
    Result=[]

    pobj= multiprocessing.Pool()
    Result=pobj.map(Square,Data)
    print("Result of square:",Result)


if __name__=="__main__":
    main()