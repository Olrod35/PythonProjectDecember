import random

heights = [random.randint(150, 200) for _ in range(10)]
heights.sort()
petya = 175
numerated = enumerate(heights)

for i, h in numerated:
    if petya < heights[0]:
        heights.insert(0, petya)
        break
    if petya > heights[-1]:
        heights.append(petya)
        break
    if petya > h:
        continue
    else:
        heights.insert(h, petya)
        heights.sort(reverse=True)
        break

print(heights)