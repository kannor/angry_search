from urllib2 import urlopen
f = open('sipder_01.txt','a')
def get_page(url):
  try:
    return str(urlopen(url).read())
  except:
    print 'Cannot open URL %s for reading' %  (url)
    f.write('Cannot open URL %s for reading\n' %  (url))
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
  all_links = []
  while True:
    url, endpos = get_next_target(page)
    if url:
      print url
      f.write(url+'\n')
      page= page[endpos:]
    else:
      break
    


#print_all_links(get_page('https://xkcd.com/352'))

def print_all_links_in_links(page):
  while True:
    url, endpos = get_next_target(page)
    
    if url:
      print
      print url;print 'going to crawl ',url
      f.write('going to crawl  ' +url+'\n')
      page= page[endpos:]
      while True:
        
        url = print_all_links(get_page(url))
        if url:
          print url
          f.write(url+'\n')
          page= page[endpos:]
        else:
          f.write('done\n')
          print 'done'
          break
    else:
      f.write('done\n')
      print 'done'
      break
print_all_links_in_links(get_page('https://xkcd.com/352'))
