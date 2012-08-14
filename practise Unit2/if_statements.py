import re
def is_friend(name):
  name1= name.lower()
  if name1[0] == 'd':
    return True
  if name1[0] == 'n' :
    return True
  return False
def biggests(a,b,c):
  if a>b>c:
    print a
  else:
    if a<b<c:
      print c
    elif b>a or c:
      print b
    else : print 'empty'

def bigger(a,b):
  if a>b:
    return a
  else: return b

def biggest(a,b,c):
  return bigger(bigger(a,b),c)
'''
i= 1
while i !=11:
  print i
  i=i+2
for i in range(4,10+1):
  print i
'''
def print_number(n):
  i= 0
  while True:
    if i>n:
      break
    
    print i
    i=i+1
def fact(n):
  results=1
  while n>=1:
    results =results*n
    n=n-1
  return results
    
