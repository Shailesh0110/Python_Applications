print("Demonstation of dictonary data type")
# Data:Hetrogeneous
# ordered:yes
# indexed:no
# Mutable:yes
#duplicates:NO

programming={'c':'ritchie','c++':'Stroustrup','Java':'Gosling','python':"Rossum"}
Batches={'PPA':18000,'LB':16700,"PYTHON":16500,"ANGULAR":15000}

print('Data of Disct:',Batches)
print("*********************")
print("DAta travels using for loop")
for x in Batches:
    print(x)

print("*********************")
print("DAta travels using for loop")
for x in Batches:
    print(x,Batches[x])


print("*********************")
print("DAta travels using for loop")
for x in Batches:
    print(x, Batches.get(x))


print("*********************")

keyBatches= Batches.keys()
print(keyBatches)
print(type(keyBatches))

valueBatches= Batches.values()
print(valueBatches)
print(type(valueBatches))

