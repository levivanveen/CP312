import json


def find_majority(A):
    n = len(A)
    majority = find_majority_helper(A, 0, n-1)
    return majority

def find_majority_helper(A, l, r):
    if l == r:
      return A[l]
    m = (l + r) // 2
    left_majority = find_majority_helper(A, l, m)
    right_majority = find_majority_helper(A, m+1, r)
    if left_majority == right_majority:
      return left_majority
    left_count = 0
    right_count = 0
    i = l
    while i <= r:
      if A[i] == left_majority:
        left_count += 1
      elif A[i] == right_majority:
        right_count += 1
      i += 1
    if left_count > (r-l+1)/2:
        return left_majority
    elif right_count > (r-l+1)/2:
        return right_majority
    else:
        return 'FAIL'


def main():
  with open('../example-arrays.json', 'r') as rf:
    data = json.load(rf)
  A3Q2 = data["A3Q2"]
  # loop through the examples in A3Q1, and check if it is equal to the hIndex at A3Q1["hIndex"]
  for example in A3Q2["examples"]:
    print(find_majority(A3Q2[example]["arr"]))

if __name__=="__main__":
    main()
