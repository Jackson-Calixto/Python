"""
order of operations: (PEDMAS)
() (Parentheses)
** (Exponent)
~ + - (unary operations)
* / % // (Division, Multiplication)
+ - (Addition, Subtraction)
>> << (shift bitwise)
& (AND bitwise)
^ | (NOT, OR bitwise)
<= < > => (comparison)
<> == != (equality)
= %= /= //= -= += *= **= (assignment)
"""

amount = 163400
time = 57.5

rate = amount / time

print('rate: '+ str(rate))

bits = 16
size = 2 ** bits

print('size: ' + str(size))

print('11 // 3: ' + str(11 // 3))
print('11 / 3: ' + str(11 / 3))
print('11 % 3: ' + str(11 % 3))
#print('11 / 0: ' + str(11 / 0))

#PEDMAS?
print(10 - 2 ** 2 / 2 + 5)
