import urllib2

url = 'https://twitter.com/yanvictords'

response = urllib2.urlopen(url)
webContent = response.read()

f = open('x.html', 'w')
f.write(webContent)
f.close