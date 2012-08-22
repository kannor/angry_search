
list = [1,2,3,4]

i = 0
while i < len(list):
  print list[i]
  i = i+1

for i in range(len(list)):
  print list[i]
  i = i + 1
# sum list
def sum_list(list):
  sum = 0
  for i in  list :#' or ' range(len(list)) :
    sum = sum+ i # 'or ' list[i]
  print 'sum ' , sum

sum_list([1,2,3,4,5])
# Measure udacity
'''
def measure_udacity(list):
  for i in range(len(list)):
    checker = list[i][0]
    #print checker
    if checker == 'U':
      print list[i]
    else:
      #print 'does not match'
      break
measure_udacity(['Uda','Una','Ama'])
'''
def measure_udacity(list):
  count = 0
  for e in list:
    if e[0]== 'U':
      count = count + 1
  return count
measure_udacity(['Uda','Una','Ama'])
# 23. find element
def find_element(list , integ):
  for e in range(len(list)):
    if list[e] == integ:
      print e
  return  '-1'
#find_element([1,2,2],3)

def find_element_index(list,integ):
  print list.index(integ)
#find_element_index([1,2,3],3)
def find_element_index_in(list,integ):
  checker = integ in list
  if checker == True:
    print list.index(integ)
  return -1
find_element_index_in([1,2,3],3)
  

