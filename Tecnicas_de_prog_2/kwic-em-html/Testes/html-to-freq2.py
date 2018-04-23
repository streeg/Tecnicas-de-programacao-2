import urllib2
import module

url = 'https://twitter.com/yanvictords'

response = urllib2.urlopen(url)
html = response.read()
text = module.stripTags(html).lower()
fullwordlist = module.stripNonAlphaNum(text)
wordlist = module.removeStopwords(fullwordlist, module.stopwords)
dictionary = module.wordListToFreqDict(wordlist)
sorteddict = module.sortFreqDict(dictionary)

for s in sorteddict: print(str(s))