# Given a list of deadlines, find the optimal order to execute tasks, where a missed deadline incurs a penalty of 100
def deadline(d, n):
  for i in range(n):
    d[i] = (d[i], i + 1)
  d_sorted = sorted(d, key=lambda x: x[0])

  # Now that deadlines are sorted, we can find order of execution
  order = [None] * n
  not_in_time = [None] * n
  penalty = 0
  time = 1

  for i in range(n):
    if time <= d_sorted[i][0]:
      order[time - 1] = (d_sorted[i][1], d_sorted[i][0])
      time += 1
    else:
      not_in_time[penalty//100] = (d_sorted[i][1], d_sorted[i][0])
      penalty += 100
  i = 0
  while not_in_time[i] != None:
    order[time - 1] = (not_in_time[i])
    time += 1
    i += 1
  # Print results
  print("The optimal execution of tasks is: ", end="")
  for d in order:
    print(d[0], ' ', end="")
  print()
  print("                        deadlines: ", end="")
  for d in order:
    print(d[1], ' ', end="")
  print()
  print("                             Time: ", end="")
  for i in range(1, n + 1):
    print(i, ' ', end="")
  print()
  print("         With a penalty of:", penalty, "\n")
  return