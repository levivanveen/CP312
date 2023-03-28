def main():
  a = [2,1,5,2,4,6,3,6,67]
  n = 9
  print(fn(a, n))

def fn(a, n):
  if n > 1:
    b = a[:n//3]
    c = a[n//3:2*(n//3)]
    d = a[2*(n//3):]
    cond2 = fn(c, n//3)
    cond3 = fn(d, n//3)
    
    if cond2:
      cond1 = fn(b, n//3)
      cond2 = (cond1 + cond2)//2
    return cond2
  else:
    return 1

if __name__=="__main__":
    main()
