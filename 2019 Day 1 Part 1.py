import numpy as np
totalFuel = 0
for x in range(100): totalFuel += (np.ceil(int(input()) / 3) - 2)
print(totalFuel)
