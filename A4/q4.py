def longest_palindrome(x, n):
  c = [[0 for i in range(n + 1)] for j in range(n + 1)]
  d = [[0 for i in range(n + 1)] for j in range(n + 1)]
  # Create string y, which is reverse of x
  y = x[::-1]
  # Fill in the rest of the table
  # Find LCS and save 'upleft', 'up', or 'left' in d
  for i in range(1, n + 1):
    for j in range(1, n + 1):
      if x[i-1] == y[j-1]:
        c[i][j] = c[i-1][j-1] + 1
        d[i][j] = 'upleft'
      elif c[i-1][j] >= c[i][j-1]:
        c[i][j] = c[i-1][j]
        d[i][j] = 'up'
      else:
        c[i][j] = c[i][j-1]
        d[i][j] = 'left'
  # Go backwards through array to find the longest palindrome
  row = n
  col = n
  pal = ''
  while row > 0 and col > 0:
    if d[row][col] == 'upleft':
      pal += x[row - 1]
      row -= 1
      col -= 1
    elif d[row][col] == 'up':
      row -= 1
    else:
      col -= 1
  return pal

def wait_for_input():
  user_input = ""
  while True:
      line = input()
      if line == "":
        break
      user_input += line + "\n"
  return user_input

def main():
  print("Please note that this program will count lowercase and uppercase letters as different characters.")
  while True:
    print("Enter a string to find the longest palindrome in it (or press enter to exit):")
    x = wait_for_input()
    if x == "":
      break
    lines = x.split("\n")
    for word in lines:
      if word == "":
        break
      n = len(word)
      print('Longest palindrome in', word, 'is', longest_palindrome(word, n))

if __name__ == '__main__':
  main()