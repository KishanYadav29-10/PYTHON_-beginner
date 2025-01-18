s ='nareshit'
print(type(s))
print(s)

s1 = '''naresh it 
technology'''
print(s1)

#python indexing always begins with 0
# python have have two different type of indexing - forward indexing and backward indexing
for i in s :
    print(i)

print(s[4])
print(s[-4])

# slicing 
print(s[0:4])
print(s[0:5])
print(s[-5:-1])
print(s[-7:6])
# advance slicing 
print(s[0:7:2])
print(s[0:6:3])

s3 = 'hello '
s4= 'world'
s5 = s3+s4
print(s5)

# operaters in python 
# -arthmatic operaters
a = 5
b = 6
c = a+b
print(c)

print(int.__add__(5,6))
print(int.__sub__(5,6))
print(int.__mul__(5,6))
# print(int.__di__(5,6))

help()

