## Questi2on 2: Greedy Algorithm, MinWeightChange problem
## 2b) calc ratio di/wi, sort by descending order, use greedy to choose coins
def ratio_greedy(d, w, v):
  ratio = []
  # Calculate ratio di/wi
  for i in range(len(d)):
    ratio.append(d[i] / w[i])
  # Greedy algorithm
  total = 0
  weight = 0
  index = find_index(ratio)
  while total < v:
    while total + d[index] > v:
      ratio[index] = -1
      index = find_index(ratio)
    total += d[index]
    weight += w[index]
  return weight


# Find the index of the largest ratio
def find_index(ratio_array):
  big = -1
  for i in range(len(ratio_array)):
    if big <= ratio_array[i]:
      big = ratio_array[i]
      index = i
  return index

## 2e) Dynamic Programming, MinWeightChange problem
def min_weight_coins(d, w, v):
  coins = [None] * (v + 1)
  coins[0] = 0
  for i in range(1, v + 1):
    min = 1000000
    for j in range(len(d)):
      # If the coin is smaller than the value and the weight is smaller than the current min
      if d[j] <= i and coins[i - d[j]] + w[j] < min:
        min = coins[i - d[j]] + w[j]
    coins[i] = min
  return coins[v]