import json

from q1 import *
from q2 import *
from q3 import *


def q1(a3):
  n = a3["n"]
  # loop through the examples in a3, and check if it is equal to the hIndex at a3["hIndex"]
  for example in a3["examples"]:
    foundHIndex = hIndex(a3[example]["arr"], 0, n - 1)
    realHIndex = a3[example]["hIndex"]
    if foundHIndex == realHIndex:
      print("Correct! h-index is: ", a3[example]["hIndex"])
    else:
      print("Incorrect! Found h-index: ", foundHIndex, " but should be: ", realHIndex)

def q2(a3):
  for example in a3["examples"]:
    print('Majority in array is:', find_majority(a3[example]["arr"]))

def q3(a3):
  for example in a3["examples"]:
    a = a3[example]["a"]
    b = a3[example]["b"]
    print('Match based on smallest difference in arrays:', greedy_smallest_diff(a,b))
    print('Match based on smallest in sorted array:', greedy_optimal_matching(a,b))

question = input('Which question do you want to run? (1, 2, or 3)\n').strip()
assignment = 'A3Q'

with open('../example-arrays.json', 'r') as rf:
  data = json.load(rf)
a3 = data[assignment + question]

print('-----------------------------\nRunning question ' + question + ':\n')
function = locals()['q' + question]

if int(question) == 1 or int(question) == 2 or int(question) == 3:
  function(a3)

