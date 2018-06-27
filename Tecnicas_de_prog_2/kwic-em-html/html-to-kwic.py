# -*- coding: utf-8 -*-

import module

# Cria um dicionario com N gramas
n = 7

# Dada a URL constroi o dicionário

url = 'https://en.wikipedia.org/wiki/Key_Word_in_Context'

#Utiliza as funcoes de module.py

text = module.webPageToText(url)
fullwordlist = ('# ' * (n//2)).split()
fullwordlist += module.stripNonAlphaNum(text)
fullwordlist += ('# ' * (n//2)).split()
ngrams = module.getNGrams(fullwordlist, n)
worddict = module.nGramsToKWICDict(ngrams)


# Pega a saida do kwic e transforma em um html.
target = 'kwic'
outstr = '<pre>'
if worddict.has_key(target):
    for k in worddict[target]:
        outstr += module.prettyPrintKWIC(k)
        outstr += '<br />'
else:
    outstr += 'Keyword nao encontrado no destino'

outstr += '</pre>'
module.wrapStringInHTMLMac('html-to-kwic', url, outstr)