v = []
z = []
l = ""
valid = 0
true = 0

numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
letters = ["a", "b", "c", "d", "e", "f"]
colours = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]

for x in range (350):
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
  v.append(k[0])


def scan(g):
  valid = 0
  for x in range (len(g)):
    true = 0
    for y in range (len(g[x])):
      m = g[x][y][4:] 
      if (g[x][y][:3] == "byr"):
        #print("byr")
        if (int(m) > 1920 and int(m) < 2002):
          true += 1
          #print("true")
      elif (g[x][y][:3] == "iyr"):
        #print("iyr")
        if (int(g[x][y][4:]) >= 2010 and int(g[x][y][4:]) <= 2020):
          true += 1
          #print("true")
      elif (g[x][y][:3] == "eyr"):
        #print("eyr")
        if (int(g[x][y][4:]) >= 2020 and int(g[x][y][4:]) <= 2030):
          #print("true")
          true += 1
      elif (g[x][y][:3] == "hgt"):
        #print("hgt")
        ht = (g[x][y][len(g[x][y]) - 2:])
        if (ht == "cm"):
          if (int(g[x][y][4:len(g[x][y]) - 2]) > 150 and int(g[x][y][4:len(g[x][y]) - 2]) < 193):
            #print("true")
            true += 1
        elif (ht == "in"):
          if (int(g[x][y][4:len(g[x][y]) - 2]) > 59 and int(g[x][y][4:len(g[x][y]) - 2]) < 76):
            #print("true")
            true += 1
        else:
          pass
      elif (g[x][y][:3] == "hcl"):
        #print("hcl")
        if (g[x][y][4] == "#"):
          hclt = 0
          for q in range (4, len(g[x][y])):
            if (g[x][y][q] in numbers or g[x][y][q] in letters):
              hclt += 1 
          if (hclt == 6):
            #print("true")
            true += 1
          else:
            pass
        else:
          pass
      elif (g[x][y][:3] == "ecl"):
        #print("ecl")
        if (g[x][y][4:] in colours):
          #print("true")
          true += 1
      elif (g[x][y][:3] == "pid"):
        #print("pid")
        if (m[0] == "0" and len(m) == 9):
          #print("true")
          true += 1
    #print(true)
    if (true == 7):
      #print(valid)
      valid += 1
  return valid

for x in range (len(v)):
  true = 0
  if (len(v[x]) == 7):
    for y in range (len(v[x])):
      if (v[x][y][:3] == "cid"):
        true += 1
    if (true == 0):
      z.append(v[x])
  elif (len(v[x]) != 8):
    pass
  else:
    z.append(v[x])
    #print(x)
    
print(len(z))
print(scan(z))


