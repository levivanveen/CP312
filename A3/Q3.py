import json


def greedy_smallest_diff(a,b):
  sum = 0
  diffList = []
  for i in range(len(a)):
    aList = []
    for j in range(len(b)):
      #make a list of the absolute value of every difference in the two arrays
      aList.append(abs(a[i] - b[j]))
    diffList.append(aList)

  while (diffList):
    #find the smallest difference in the list of differences
    min = (-1, -1, -1)
    for i in range(len(diffList)):
      for j in range(len(diffList[i])):
        if min[0] < 0 or diffList[i][j] < min[0]:
          min = (diffList[i][j], i, j)
    sum += min[0]**2
    diffList.pop(min[1])
    for i in range(len(diffList)):
      diffList[i].pop(min[2])
  return sum

def greedy_optimal_matching(a,b):
  sum = 0
  a.sort()
  b.sort()
  for i in range(len(a)):
    sum += (a[i] - b[i])**2
  return sum


def main():
  with open('../example-arrays.json', 'r') as rf:
    data = json.load(rf)
  a3Q3 = data["A3Q3"]
  for example in a3Q3["examples"]:
    if (example == "example1"):
      a = a3Q3[example]["a"]
      b = a3Q3[example]["b"]
      print(greedy_smallest_diff(a,b))

if __name__=="__main__":
  main()
