# type casting
# covert one datatype to another datatype

print(int(2.3))
# print(int(2.3,7.5)) # type casting into integer is done for each parameter or argument
print(int(2.3),int(10.5)) 
print(int(True))
# print(int(1+2j)) #we cannot type cast complex to integer    
print(int('10'))
# # print(int('ten')) ---> type casting doesn't work if the input is not im the form of number inside string
# # parameter == argument
print(float('10'))
# print(float(10,5))  --> type casting into float is done for each parameter or argument
print(float(10))
print(float(True))
print(float(False))

print(complex(1))
print(complex(1,2)) # when type casting  into complex (1 and 2) parameter or argument can be passed
print(complex(1.5,2)) 
print(complex(True,False)) 
print(complex(False,True)) 
print(complex('1'))

print(str(10))
print(str(10.5))
print(str(True))
# print(str(10,20)) # type casting into str is done for each parameter or argument

print(bool(1))
print(bool(10))
print(bool(5)) #non zero is True
print(bool(0))
print(bool( ))
print(bool(2+7j))
print(bool(2+0j))