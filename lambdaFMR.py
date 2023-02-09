
from functools import  reduce

def main():
    print("enter no of elements you want to enter:")
    isize = int(input())
    Data_Input = []
    print("please enter the data")
    for iCnt in range(0, isize, 1):
        value = int(input())
        Data_Input.append(value)

    print("Data is: ", Data_Input)

    Data_Filter=list(filter(lambda no: (no%2==0),Data_Input))

    print("Data after filter is :",Data_Filter)

    Data_map=list(map(lambda no:no*2,Data_Filter))
    print("Data after map:",Data_map)

    output=reduce(lambda a,b:a+b,Data_map)
    print("Result after reduce is :",output)



if __name__=="__main__":   #starter plate match
    main()