# Arithmetic Operators
num1 = 3 
num2 = 2
print(num1+num2)
print(num1-num2)
print(num1*num2)
print(num1/num2)
print(num1%num2)
print(num1//num2)
print(num1**num2)


# compound assignment operators
num = 10
#num = num + 5
num+=5
print(num)
num*=5
print(num)

# comparison / Relational Operators
num1 = 3
num2 = 2

print(num1>num2)
print(num1<num2)
print(num1!=num2)

# logical operations
a = 10 
b = 5 
c = 3
d = 8

result_and = a > b and b < c 
print(result_and)
result_or = a > b or b < c 
print(result_or)
result_not = a > b
print(not result_not)

# membership operations 
text = "python is eazy"
is_z_present = "z" in text
print(is_z_present)

list_nums = [1,2,3,4,5]
is_5_present = 5 in list_nums
print(is_5_present)


is_z_not_present = "z" not in text
print(is_z_not_present)

# Identity Operators
num1 = 10 
num2 = 10 
print(id(num1))
print(id(num2))
print(num1 is num2)


num1_list = [10,20]
num2_list = [10,20]
print(id(num1_list))
print(id(num2_list))
print(num1_list is num2_list)

print(num1_list is not num2_list)

# bitwise operators 

a = 5 
b = 3 
resultand = a & b 
print(resultand)

resultor = a | b 
print(resultor)

resultxor = a ^ b 
print(resultxor)

resultnot = ~b
print(resultnot)

b = 3 
print(3<<2)
print(3<<1)
print(3<<3)


b = 3

print(3>>2)
print(3>>1)
print(8>>2)

c = -4 

print(-4>>3)