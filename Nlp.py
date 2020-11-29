from hazm import *

#Make the code simpler
stopwords=stopwords_list("Persian_stopwords.txt")
sent='فردا هوای تهران و شیراز چند درجه  خواهد شد؟'
print(sent)
normalizer = Normalizer()
sent=normalizer.normalize(sent)
token=word_tokenize(sent)
sentence=[]
for w in token:
    if w not in stopwords:
        sentence.append(w)
print(sentence)
for word in sentence:
    print(Lemmatizer().lemmatize(word))
