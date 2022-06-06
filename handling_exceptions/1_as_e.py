(x,y) = (5,0)
try:
   z = x/y
except ZeroDivisionError as e:
   z = e # representation: "<exceptions.ZeroDivisionError instance at 0x817426c>"
print(z) # output: "integer division or modulo by zero"
