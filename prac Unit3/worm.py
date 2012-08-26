from urllib2 import urlopen

#opens an url

def open_url(url):
    try:
        return str(urlopen(url).read())
    except:
        #print 'cannot open %s for reading' % (url)
        return ''
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


def crawl_web(seed):
    tocrawl = [seed]
    crawled = []
    while tocrawl:
        page = tocrawl.pop()
        if page not in crawled:
            union(tocrawl,get_link(open_url(page)))
            crawled.append(page)
    print  crawled
#get_link(open_url('http://www.ug.edu.gh'))
crawl_web('http://xkcd.com/')
            
