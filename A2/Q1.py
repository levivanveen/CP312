import json


def main():
  with open('../example-arrays.json', 'r') as rf:
    data = json.load(rf)

  a2q1 = data["A2Q1"]
  n = a2q1["n"]
  for example in a2q1["examples"]:
    arr1 = a2q1[example]["array1"]
    arr2 = a2q1[example]["array2"]
    print(twoWayTwoSum(arr1, arr2, n))
    print()

def twoWayTwoSum(arr1, arr2, n):
  addArr = []
  # n^2 so far if sorting doesnt matter
  for i in range(n):
    for j in range(n):
      addArr.append(arr1[i] + arr1[j])

  addArr.sort()

  for i in range(n):
    for j in range(n):
      print('looking for', arr2[i] + arr2[j])
      if (arr2[i] + arr2[j]) in addArr: 
        print('found it')
        return True

if __name__=="__main__":
    main()