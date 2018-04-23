import urllib2

url = 'https://twitter.com/yanvictords'

response = urllib2.urlopen(url)
webContent = response.read()

print(webContent[0:300])