print("Demonstation of set data type")
# Data:Hetrogeneous
# ordered:NO
#  indexed:NO
# Mutable:yes
#duplicates:NO

data= {11,21,51,101,21,11} # duplicates
data1={11,90.8,"hello",True}  # hetrogeneous

print(data)
print(len(data))
print('data in hetrogeneous:',data1)
print('data in orderd :',data1)
#print("Data at index :2",data1[2])
print('data with uniqe elements :',data)


print('set is mutable')
#insert elemet in set
data.add(211)
print('data after isertion:',data)

# remove element
data.remove(211)
print('data after removal:',data)

data.discard(201)
print('data after discard:',data)


