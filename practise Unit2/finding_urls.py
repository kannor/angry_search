'''
page = '<a href="http://facebook.com">facebook</a>'
def get_next_target(page):
    start_link = page.find("<a href=")
    start_quote = page.find('"',start_link)
    end_quote = page.find('"',start_quote+1)
    url = page[start_quote+1:end_quote]
    return  url, end_quote
    #print url
    #print page[end_quote:]
def rest_of_string(s):
  return s[2:]
def sum(a,b):
  a=a+b
  return a
def find_sec(a,b):
  first=a.find(b)
  second = a.find(0
'''

  
  
def first(a,b,c):
  sum=a+b+c
  return sum


def second():
  return first(1,2,3)
def friend(a):
  if a[0:1] == 'd':
    print 'True'
  else:print 'false'
