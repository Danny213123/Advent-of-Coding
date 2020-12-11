k = []
for x in range (200):
  k.append(int(input()))
  if (k[-1] is None):
    print(x)
    break

for y in range (len(k)):
  for q in range (len(k)):
    for l in range(len(k)):
      if (k[y] + k[q] + k[l] == 2020):
        print(k[y] * k[q] * k[l])
