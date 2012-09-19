from urllib2 import urlopen
execfile("open_url.py")
#opens an url
'''
def open_url(url):
    try:
        return str(urlopen(url).read())
    except:
        print 'cannot open %s for reading or invalid url' % (url)
        return ''
'''
def union(link_a,link_b):
    #list_a = []
    for url in link_b:
        if url not in link_a:
            link_a.append(url)
    return link_a
    

def link_extractor(page):
    start_link = page.find("<a href=")
    if start_link == -1:
        return None,0
    else:
        start_quote = page.find('"',start_link)
        end_quote = page.find('"',start_quote + 1)
        url = page[start_quote + 1: end_quote]
        return url , end_quote

def get_link(page):
    links = []
    while True:
        url , endpos = link_extractor(page)
        if url:
            #print url
            links.append(url)
            page = page[endpos:]
        else:
            break
    #print links
    return (links)





    
# this procedure checks the maximum number of pages to crawl
def crawl_web1(seed, max_pages):
    #max_pages = 5
    tocrawl = [seed]
    crawled = []
    while tocrawl:
        page = tocrawl.pop()
        if page not in crawled and len(crawled) < max_pages:
            union(tocrawl,get_link(open_url(page)))
            crawled.append(page)
    print  crawled
    print len(crawled)
# this procedure checks for the maximum depth to crawl.....
# same proceure as the one above

def crawl_web2(seed,max_depth):
    #max_depth = 5
    tocrawl = [seed]
    crawled = []
    next_depth = []
    depth = 0
    
    while tocrawl and depth <= max_depth:
        page = tocrawl.pop()
        if page not in crawled :
            union(next_depth,get_link(open_url(page)))
            crawled.append(page)
        if not tocrawl :
            tocrawl, next_depth = next_depth , []
            depth = depth + 1
    print  crawled
    
    print len(crawled)
index = []
def add_to_index(index,keyword,url):
    for e in index:
        if e[0] == keyword:
            if not url in e[1]:
                e[1].append(url)
            return
    #if not found add a new entry
    index.append([keyword,[url]])
    


def add_page_to_index(index,url,content):
    words = content.split()
    for word  in words:
        add_to_index(index,word,url)
'''
        for e in index:
            if e[0] == word:
                e[1].append(url)
                #return
        index.append([word,[url]])
'''
def crawl_web(seed,max_pages):
    #max_pages = 5
    tocrawl = [seed]
    crawled = []
    index =[]
    while tocrawl:
        page = tocrawl.pop()
        if page not in crawled and len(crawled) < max_pages:
            content = open_url(page)
            add_page_to_index(index,page,content)
            union(tocrawl,get_link(content))
            crawled.append(page)
    print crawled
    print content
    print index
    return index
    



def lookup(index,keyword):
    for e in index:
        if e[0] == keyword:
            return e[1]
        
    return []


crawl_web('http://www.xkcd.com/',1)
'''
add_page_to_index(index,'fake.com',"This is a test")
#print index
add_page_to_index(index,'not.com',"This is not a test man")
add_page_to_index(index,'come.com',"This is not a test man")
add_page_to_index(index,'fb.com.',"This is not a test for women")
print index


add_page_to_index(index,'http://dilbert.com',
                  """
Another Strategy is to ignore the fact that you are slowly killing yourself
by not sleeping and exercising enough. That frees up several hours a day.
The only downsides is that you get fata and die.
-- Scott Adams on Time Management""")

add_page_to_index(index,'http://randy.pausch',
                  """
                  Good judgment comes from experience, experience comes from bad
                  judgement. If things aren't going well it probably means you are
                  learning a lot and things wil go better latterr.
                    ---Randy Pausch
                  """)

print index
'''
#get_link(open_url('http://www.ug.edu.gh'))
#crawl_web('http://www.facebook.com/',100)
#crawl_web2('http://www.facebook.com/',10)
            
