
#normal functions or named functions
def add(no1,no2):
    return no1+no2

#lambda function/unnamed function
#lambda parameters:body

addfunction=lambda a,b:a+b

ans1=add(10,11)
ans2=addfunction(10,11)
print("addition of normal function:",ans1)
print("addition of lambda function:",ans2)

print("type of lambd function :",type(addfunction))
