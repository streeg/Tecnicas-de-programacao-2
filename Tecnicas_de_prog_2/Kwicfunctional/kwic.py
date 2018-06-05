import re

# -*- coding: utf-8  -*-


def stripNonAlphaNum(x):
    return re.sub(r'[^a-zA-Z: ]', '', x) # x is my string to sanitize
    #re.compile(r'\W+', re.UNICODE).split(text)

def removeStopwords(wordlist, stopwords):
    return [w for w in wordlist if w not in stopwords]

wordlist = open('test.txt', 'r').read().split()
stoplist = open('stopwords.pt', 'r').read().split()
#print(wordlist)
wordlist = map(lambda x:x.lower(), wordlist)
wordlist = map(stripNonAlphaNum, wordlist)
wordlist = removeStopwords(wordlist, stoplist)

ngrams = [wordlist[i:i+5] for i in range(len(wordlist)-4)]

kwicdict = {}
for n in ngrams:
    if n[2] not in kwicdict:
        kwicdict[n[2]] = [n]
    else:
        kwicdict[n[2]].append(n)

#print kwicdict



for key in sorted(kwicdict.iterkeys()): 
    for val in kwicdict[key]:

       outstring = ' '.join(val[:2]).rjust(20)
       outstring += ' '
       outstring += ' '.join(str(val[2]).center(len(n[2])+6))
       outstring +=' '
       outstring += ' '.join(val[3:])
       print outstring


