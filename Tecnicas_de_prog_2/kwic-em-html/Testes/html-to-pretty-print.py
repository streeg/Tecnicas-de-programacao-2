# html-to-pretty-print.py
import module

# create dictionary of n-grams
n = 10
url = 'https://twitter.com/yanvictords'


text = module.webPageToText(url)
fullwordlist = module.stripNonAlphaNum(text)
ngrams = module.getNGrams(fullwordlist, n)
worddict = module.nGramsToKWICDict(ngrams)

print(worddict["fechar"])