import urllib2, module

url = 'https://twitter.com/yanvictords'

response = urllib2.urlopen(url)
html = response.read()
text = module.stripTags(html).lower()
wordlist = module.stripNonAlphaNum(text)
dictionary = module.wordListToFreqDict(wordlist)
sorteddict = module.sortFreqDict(dictionary)

for s in sorteddict: print(str(s))