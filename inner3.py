def Add(A,B):
    return A+B
def Sub(A,B):
    return A-B
def Calculator(target,Value1,Value2):
    return target(Value1,Value2)

Ret=Calculator(target=Add,Value1=10,Value2=11)
print("Addition is :",Ret)

Ret=Calculator(target=Sub,Value1=10,Value2=11)
print("Addition is :",Ret)
