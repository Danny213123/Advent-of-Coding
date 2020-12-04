g = []
l = ""
valid = 0
true = 0

for x in range (340):
  k =[[]]
  for y in range (50):
    try:
      l = input()
      if (l == ""):
        break

      l = l.split()
      k[0] += l
    except EOFError as error:
      continue
  g.append(k[0])

for x in range (len(g)):
  true = 0
  z = []
  if (len(g[x]) == 7):
    for y in range (len(g[x])):
      if (g[x][y][:3] == "cid"):
        true += 1
    if (true == 0):
      valid += 1
  elif (len(g[x]) != 8):
    pass
  else:
    valid += 1
    #print(x)
    
print(valid)
