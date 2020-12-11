k = []
for x in range (200):
  k.append(int(input()))
  if (k[-1] is None):
    print(x)
    break

for y in range (len(k)):
  s = 2020 - k[y]
  if s in k:
    print (s * k[y])
  else:
    pass  
