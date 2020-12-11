answers = []
z = []
l = ""
score_storage = []

for x in range (474):
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
  answers.append(k[0])

for x in range (len(answers)):
  temp_storage = ""
  score = 0
  for y in range (len(answers[x])):
    for d in range (len(answers[x][y])):
      if (answers[x][y][d] not in temp_storage):
        temp_storage += answers[x][y][d]
      else:
        pass
  for i in range (len(temp_storage)):
    true = 0
    for j in range (len(answers[x])):
      if (temp_storage[i] in answers[x][j]):
        true += 1
    if (true == len(answers[x])):
      score += 1
  score_storage.append(score)

total_score = 0

for l in range (len(score_storage)):
  total_score += int(score_storage[l])

print(total_score)
