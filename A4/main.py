import json

from q1 import *
from q2 import *
from q3 import *
from q4 import *


def q1(a4):
  for example in a4["examples"]:
    deadline(a4[example]["arr"], a4[example]["n"])
  return

def q2(a4):
  for example in a4["examples"]:
    ratio = []
    min_weight = []
    for value in a4["values"]:
      ratio.append(ratio_greedy(a4[example]["d"], a4[example]["w"], value))
      min_weight.append(min_weight_coins(a4[example]["d"], a4[example]["w"], value))
    print("Example: ", example)
    for i in range(len(ratio)):
      if ratio[i] == min_weight[i]:
        print("Value is", a4["values"][i], ": ", ratio[i])
      else:
        print("Value is", a4["values"][i], ": ", ratio[i], min_weight[i])
    print()
  return

def q3(a4):
  for example in a4["examples"]:
    print("The element that appears once in:", a4[example]["arr"])
    print("is:", not_twice(a4[example]["arr"], 0, len(a4[example]["arr"])))
    print()
  return
    
def q4(a4):
  for example in a4["examples"]:
    print("The longest palindrome in:", a4[example]["x"])
    print("is:", longest_palindrome(a4[example]["x"], len(a4[example]["x"])))
    print()

question = input('Which question do you want to run? (1, 2, 3, or 4)\n').strip()
assignment = 'A4Q'

with open('/Users/levivanv/Documents/GitHub/CP312/example-arrays.json', 'r') as rf:
  data = json.load(rf)
a4 = data[assignment + question]

print('-----------------------------\nRunning question ' + question + ':\n')
function = locals()['q' + question]

if int(question) == 1 or int(question) == 2 or int(question) == 3 or int(question) == 4:
  function(a4)