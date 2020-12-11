import math

rowid = []
for x in range (945):
  k = input()

  row, col = 0, 0

  min2, max2 = 0, 7
  min, max = 0, 127
  for y in range (len(k) - 3):
    if (k[y] == "F"):
      max = math.floor((max + min) / 2)
    elif (k[y] == "B"):
      min = math.ceil((max + min) / 2)
    row = max
  for d in range (len(k) - 3, len(k)):
    if (k[d] == "L"):
      max2 = math.floor((max2 + min2) / 2)
    elif (k[d] == "R"):
      min2 = math.ceil((max2 + min2) / 2)
    col = max2
  rowid.append((row * 8) + col)

rowid.sort()
error_id = 0

for l in range (2, len(rowid) - 2):
  previous_id = rowid[l - 1]
  current_id = rowid[l]
  next_id = rowid[l + 1]

  if (current_id - previous_id > 1 or next_id - current_id > 1):
    error_id += current_id

print(error_id / 2)
