answers = []
unique_answers = []
score = []

#474
for x in range (474):
  k = []
  l = ""
  for y in range (50):
    try:
      get_input = input()

      if (get_input == ""):
        break
      l += get_input

    except EOFError as error:
      continue
  k.append(l)
  answers.append(k)

for x in range (len(answers)):
  temp_storage = ""
  for y in range (len(answers[x])):
    for d in range (len(answers[x][y])):
      if (answers[x][y][d] not in temp_storage):
        temp_storage += answers[x][y][d]
      else:
        pass
  score.append(len(temp_storage))
  
total_score = 0

for l in range (len(score)):
  total_score += int(score[l])

print(total_score)
