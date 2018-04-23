import urllib2, module

url = 'https://twitter.com/yanvictords'

response = urllib2.urlopen(url)
HTML = response.read()

print(module.stripTags(HTML))