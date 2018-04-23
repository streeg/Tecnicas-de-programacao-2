import module

test = 'this test sentence has eight words in it'
ngrams = module.getNGrams(test.split(), 5)

print(module.nGramsToKWICDict(ngrams))