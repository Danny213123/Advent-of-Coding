k = []

for x in range (323):
  k.append(input())

k.append("." * len(k[0]))

done = False
trees = [0], [0], [0], [0], [0]

directionsx = [1], [3], [5], [7], [1]
directionsy = [1], [1], [1], [1], [2]

for x in range (len(directionsx)):
  done = False
  currenty, currentx = 0, 0
  while (done == False):
    
    if (currenty > len(k) - 1):
      done = True
      break
    if (k[currenty][currentx] == "#"):
      trees[x][0] += 1
    if (currentx + directionsx[x][0] > len(k[currenty]) - 1):
      temp = abs(len(k[currenty]) - (currentx + directionsx[x][0]))
      currentx = temp
    else:
      currentx += directionsx[x][0]

    if (currenty + directionsy[x][0] > len(k)):
      done = True
      break
    else:
      currenty += directionsy[x][0]

print(trees[0][0] * trees[1][0] * trees[2][0] * trees[3][0] * trees[4][0])
