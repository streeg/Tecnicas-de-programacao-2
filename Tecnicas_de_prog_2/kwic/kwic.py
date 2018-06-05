#Import para o modulo para remover caracteres especiais
import re

#-*- coding: utf-8  -*-

#Funcao que remove caracteres nao alfa numericos
def stripNonAlphaNum(x):
    return re.sub(r'[^a-zA-Z: ]', '', x) # x is my string to sanitize


#Remove as stopwords que ja foram abertas na execucao do programa.
def removeStopwords(wordlist, stopwords):
    return [w for w in wordlist if w not in stopwords]

#abre o texto para executar o kwic e salva em uma lista com todas as palvras
wordlist = open('test.txt', 'r').read().split()
#abre as stopwords em portugues com o .pt e ingles com o .en
#todo: linkar as diferentes opcoes com o programa checkbox.py
stoplist = open('stopwords.pt', 'r').read().split()
#coloca as palavras em caixa-baixa
wordlist = map(lambda x:x.lower(), wordlist)
#chama a funcao para remocao de caracteres alfa-numericos
wordlist = map(stripNonAlphaNum, wordlist)
#chama a funcao para a remocao de stopwords
wordlist = removeStopwords(wordlist, stoplist)
#Separa de 5 em 5 palavras de wordlist em uma nova lista
ngrams = [wordlist[i:i+5] for i in range(len(wordlist)-4)]
#organiza o kwic para mostrar as palavras mais frequentes e constroi um dicionario (chave = palavra, valor = frequencia)
kwicdict = {}
for n in ngrams:
    if n[2] not in kwicdict:
        kwicdict[n[2]] = [n]
    else:
        kwicdict[n[2]].append(n)

#por ordem de frequencia, imprime da mais frequente para a menos as palavras do dicionario anteriormente construido.
for key in sorted(kwicdict.iterkeys()):
    for val in kwicdict[key]:
#deixa bonito
       outstring = ' '.join(val[:2]).rjust(20)
       outstring += ' '
       outstring += ' '.join(str(val[2]).center(len(n[2])+6))
       outstring +=' '
       outstring += ' '.join(val[3:])
       print outstring
