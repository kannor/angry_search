def open_url(url):
    try:
        return str(urlopen(url).read())
    except:
        print 'cannot open %s for reading or invalid url' % (url)
        return ''
