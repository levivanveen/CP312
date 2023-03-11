import json


def main():
  with open('../example-arrays.json', 'r') as rf:
    data = json.load(rf)
  q2 = data["A2Q2"]
  n = q2["n"]
  for x in q2["examples"]:
    right = findRight(q2[x]['arr'], 0, n)
    left = findLeft(q2[x]['arr'], 0, right)
    print(left, right, 'found em')

def findRight(arr, start, end):
  middle = (end + start)//2
  left = middle - 1
  right = middle + 1
  if arr[middle] >= arr[left]:
    if arr[middle] > arr[right]:
      return middle
    else:
      return findRight(arr, right, end)
  else:
    return findRight(arr, start, left)

def findLeft(arr, start, end):
  middle = (end + start)//2
  left = middle - 1
  right = middle + 1
  if arr[middle] >= arr[right]:
    if arr[middle] > arr[left]:
      return middle
    else:
      return findLeft(arr, start, left)
  else:
    return findLeft(arr, right, end)

if __name__=="__main__":
    main()