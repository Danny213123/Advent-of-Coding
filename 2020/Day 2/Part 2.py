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
  if (String[int(Min) - 1] == Letter or String[int(Max) - 1] == Letter):
    if (String[int(Min) - 1] == Letter and String[int(Max) - 1] == Letter):
      pass
    else:
      valid += 1

print(valid)
