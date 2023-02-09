
#Logic
def checkeven(no):
    return (no%2==0)

def Doubles(no):
    return no*2

def sum(a,b):
    return a+b

#**********************************
# fuction make

def filterX(Helper_function,Data):
    result=[]
    for no in Data:
        if (Helper_function(no)==True):
            result.append(no)

    return result

def mapX(helper_function,Data):
    result=[]
    for no in Data:
        value=helper_function(no)
        result.append(value)

    return result

def reduceX(helper_fuction,Data):
    ans=0
    for no in Data:
        ans=helper_fuction(ans,no)

    return ans

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

    Data_Filter=filterX(checkeven,Data_Input)

    print("Data after filter is :",Data_Filter)

    Data_map=mapX(Doubles,Data_Filter)
    print("Data after map:",Data_map)

    output=reduceX(sum,Data_map)
    print("Result after reduce is :",output)

#**********************************
# call main fuction

if __name__=="__main__":   #starter plate match
    main()