from urllib2 import urlopen
f = open('f.txt','w')
def get_page(url):
  try:
    return str(urlopen(url).read())
  except:
    return ""
page = get_page('http://xkcd.com/365')

def get_next_target(page):
  start_link = page.find("<a href=")
  if start_link== -1:
    return None,0
  
  else:
    start_quote = page.find('"',start_link)
    end_quote = page.find('"',start_quote+1)
    url = page[start_quote+1:end_quote]
    return  url, end_quote

'''
url, endpos = get_next_target(page)
if url:
  print 'Here',url

else:
  print 'not here'
'''
def print_all_links(page):
  while True:
    url, endpos = get_next_target(page)
    if url:
      print url #f.write(url)
      page= page[endpos:]
    else:
      break


print_all_links(get_page('https://github.com/fhim50'))
