# -*- coding: utf-8 -*-

import module

# create dictionary of n-grams
n = 7
url = 'https://en.wikipedia.org/wiki/Key_Word_in_Context'

text = module.webPageToText(url)
fullwordlist = ('# ' * (n//2)).split()
fullwordlist += module.stripNonAlphaNum(text)
fullwordlist += ('# ' * (n//2)).split()
ngrams = module.getNGrams(fullwordlist, n)
worddict = module.nGramsToKWICDict(ngrams)


# output KWIC and wrap with html
target = 'kwic'
outstr = '<pre>'
if worddict.has_key(target):
    for k in worddict[target]:
        outstr += module.prettyPrintKWIC(k)
        outstr += '<br />'
else:
    outstr += 'Keyword not found in source'

outstr += '</pre>'
module.wrapStringInHTMLMac('html-to-kwic', url, outstr)