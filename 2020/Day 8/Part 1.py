accumulator = 0

l = []

for x in range (654):
  try:
    s = {}
    a, b = input().split()
    s['type'] = a
    s['other'] = b
  except EOFError as error:
    continue
  l.append(s)

print(l[0]['type'])

past_operation = []
debug_operation = []
current_operation = "0"

while (current_operation not in past_operation):
  print(accumulator)
  past_operation.append(current_operation)
  temp_operation = int(current_operation)
  debug_operation.append(temp_operation)
  if (l[temp_operation]['type'] == 'acc'):
    if (l[temp_operation]['other'][0] == "+"):
      accumulator += int(l[temp_operation]['other'][1:])
      temp_operation += 1
    else:
      accumulator -= int(l[temp_operation]['other'][1:])
      temp_operation += 1
  elif(l[temp_operation]['type'] == "jmp"):
    if (l[temp_operation]['other'][0] == "+"):
      temp_operation += int(l[temp_operation]['other'][1:])
    else:
      temp_operation -= int(l[temp_operation]['other'][1:])
  else:
    temp_operation += 1
  current_operation = str(temp_operation)


debug_operation.sort()
print(debug_operation)
