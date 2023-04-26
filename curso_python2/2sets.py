list1 = [10, 20, 30, 40, 50]
list2= [10, 20, 60, 70, 80]

#set perde a indexação
num1 = set(list1)
num2 = set(list2)

print(num1 | num2) #União  union
print(num1 - num2) #diferença - difference
print(num1 ^ num2) # simetrico - symmetric (valores unicos que não são repetidos)
print(num1 & num2) #and um e outro
print(len(num1))

