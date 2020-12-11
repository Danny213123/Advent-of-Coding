import numpy as np

def Recursion(n):
  if (n <= 0):
    return n
  else:
    a = np.ceil(n / 3)
    a -= 2
    return (a + Recursion(a))

b=0
for x in range (100):
  b+=Recursion(int(input()))
  
print(b)
