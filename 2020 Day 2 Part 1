r = []
for q in range (1000):
  k = (input())
  k = k.replace("-", " ")
  k = k.replace(":", "")
  r.append(k.split())

valid = 0

for x in range (len(r)):
  counter = 0
  Min, Max, Letter, String = r[x][0], r[x][1], r[x][2], r[x][3]
  for y in range (len(String)):
    if (String[y] == Letter):
      counter += 1
  if (counter >= int(Min) and counter <= int(Max)):
    valid += 1

print(valid)

