
from functools import  reduce
#Lambda
checkeven=lambda no: (no%2==0)


Doubles=lambda no:no*2


sum=lambda a,b:a+b


#**********************************

#**********************************
# calling fuctions

def main():
    print("enter no of elements you want to enter:")
    isize = int(input())
    Data_Input = []
    print("please enter the data")
    for iCnt in range(0, isize, 1):
        value = int(input())
        Data_Input.append(value)

    print("Data is: ", Data_Input)

    Data_Filter=list(filter(checkeven,Data_Input))

    print("Data after filter is :",Data_Filter)

    Data_map=list(map(Doubles,Data_Filter))
    print("Data after map:",Data_map)

    output=reduce(sum,Data_map)
    print("Result after reduce is :",output)

#**********************************
# call main fuction

if __name__=="__main__":   #starter plate match
    main()