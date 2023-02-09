
def checkeven(no):
    return (no%2==0)

def increment(no):
    return no+2



def filterX(Arr,fuction_name):
    result=[]
    for no in Arr:
        if(fuction_name(no)):
            result.append(no)
    return result

def mapX(Arr,function_name):
    result=[]
    for no in Arr:
        value=function_name(no)
        result.append(value)
    return result

def reduceX(Arr):
    sum=0
    for no in Arr:
        sum=sum+no
    return  sum


def main():
    data=[2,3,1,6,4,5,11,16,20]

    print("original data",data)
    data_filter=list(filterX(data,checkeven))
    print("data_filter:",data_filter)

    data_map=list(mapX(data_filter,increment))
    print("data map",data_map)

    ret=reduceX(data_map)
    print("data reduce:",ret)


if __name__=="__main__":
    main()