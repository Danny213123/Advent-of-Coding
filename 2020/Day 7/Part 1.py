bag_storage = []
contain_info_storage = []
length = 39

for x in range (length):
  try:
    hash = {}
    contain_info = []
    line = input().split()
    hash['bag_type'] = line[0] + line[1]

    for x in range (4, len(line) - 2, 4):
      contain_info.append(line[x] + line[x + 1] + line[x + 2])

    hash['contain_info'] = contain_info

    bag_storage.append(hash)
  except EOFError as error:
    continue

# Sort by bag_type
def get_bag_type(dict):
  return dict['bag_type']

l = []

def graph_theory(graph):
  if (graph == "shinygold"):
    return graph
  print(graph)
  for x in range (length):
    if (graph[1:] in bag_storage[x]['bag_type']):
      print(x)
      for d in range (len(bag_storage[x]['contain_info'])):
        return 
  return "nope"

shiny_gold = 0
bag_vector = []

print(graph_theory('mutedbronze'))

def k():
  # Scan the bags
  for x in range (length):
    print(bag_storage[x]['contain_info'])
    temp_holding = []

    # Scan what the bag can hold
    for y in range (len(bag_storage[x]['contain_info'])):
      current_bag = bag_storage[x]['contain_info'][y]

      bag_vector[0]

      # Scan through
      for d in range (length):
        if (current_bag[1:] in bag_storage[d]['bag_type']):
          print(d)
      


#print(bag_storage[0]['bag_type'])
#print(bag_storage[0]['contain_info'])
