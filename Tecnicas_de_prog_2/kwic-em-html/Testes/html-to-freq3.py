import module

# create sorted dictionary of word-frequency pairs
url = 'https://twitter.com/yanvictords'

text = module.webPageToText(url)

fullwordlist = module.stripNonAlphaNum(text)
wordlist = module.removeStopwords(fullwordlist, module.stopwords)
dictionary = module.wordListToFreqDict(wordlist)
sorteddict = module.sortFreqDict(dictionary)

# compile dictionary into string and wrap with HTML
outstring = "wikipedia"
for s in sorteddict:
    outstring += str(s)
    outstring += "<br />"

module.wrapStringInHTMLMac("html-to-freq-3", url, outstring)