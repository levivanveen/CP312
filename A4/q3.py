# Given an array of integers, every element appears twice except for one. Find that single one.
# Idea is that in parts of array before single element, pairs have even index then odd. after switches it
def not_twice(a, l, r):
  mid = (l + r) // 2
  
  # Base case: middle item is not adjacent to equal items
  if check_left_and_right(a, mid, r): return a[mid]

  # Need to check if mid is even or odd
  if mid % 2 == 0:
    search_right = a[mid] == a[mid + 1]
    first_in_pair = search_right
  else:
    search_right = a[mid] == a[mid - 1]
    first_in_pair = not search_right
  
  if search_right:
    # If mid is the index of the 1st item in a pair, we can increment it by 1
    return not_twice(a, mid + 1 if first_in_pair else mid, r)
  else:
    # If mid is the index of the second item in a pair, we can decrement it by 1
    return not_twice(a, l, mid - 1 if not first_in_pair else mid)
  

def check_left_and_right(arr, index, n):
  if index == 0: return arr[index] != arr[index+1]
  elif index == n-1: return arr[index] != arr[index-1]
  else: return arr[index] != arr[index-1] and arr[index] != arr[index+1]
