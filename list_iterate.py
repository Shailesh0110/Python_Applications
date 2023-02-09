
data =[11,21,51,101]
print('output using for')
for no in data:
    print(no,end=" ")  # end= same line
print('\n---------------')

print('output using for with index')
for i in range(0,len(data)):
    print(data[i],end=" ")  # end= same line
print('\n---------------')

print('output using while with index')
i=0
while(i<len(data)):
    print(data[i],end=" ")
    i=i+1
print('\n---------------')