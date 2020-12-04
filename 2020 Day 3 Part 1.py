k = []

for x in range (323):
  k.append(input())

k.append("." * len(k[0]))

currenty, currentx, trees = 0, 0, 0

while (currenty != len(k) - 1):
  if (k[currenty][currentx] == "#"):
    trees += 1;
  if (currentx + 3 > len(k[currenty]) - 1):
    temp = abs(len(k[currenty]) - (currentx + 3))
    currentx = temp
  else:
    currentx += 3

  if (currenty + 1 > len(k)):
    break
  else:
    currenty += 1

print(trees)
