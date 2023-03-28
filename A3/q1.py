import json


def hIndex(arr, start, end):
  # Base case
  if (end - start <= 1):
    if arr[end] >= end + 1:
      return end + 1
    elif arr[start] >= start + 1:
      return start + 1
    else:
      return start
  # Recursive case
  mid = (start + end) // 2
  if (arr[mid] == mid + 1):
    return mid + 1
  elif arr[mid] > mid + 1:
    return hIndex(arr, mid, end) 
  else:
    return hIndex(arr, start, mid)

def main():
  with open('../example-arrays.json', 'r') as rf:
    data = json.load(rf)
  A3Q1 = data["A3Q1"]
  n = A3Q1["n"]
  # loop through the examples in A3Q1, and check if it is equal to the hIndex at A3Q1["hIndex"]
  for example in A3Q1["examples"]:
    if hIndex(A3Q1[example]["arr"], 0, n - 1) == A3Q1[example]["hIndex"]:
      print("Correct!")
    else:
      print("Incorrect!")



if __name__=="__main__":
    main()
