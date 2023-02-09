print("Demonstation of List data type")


# Data:Hetrogeneous
# ordered:yes
#  indexed:yes
# Mutable:yes
#duplicates:yes

data= [11,21,51,101,21,11] # duplicates
data1=[11,90.8,"hello"]  # hetrogeneous

print('data in orderd ',data1)
print("Data at index :2",data1[2])
print('data with duplicates :',data)


print('list is mutable')
data.append(201)
print('data after append:',data)

data.pop()
print('data after pop:',data)





