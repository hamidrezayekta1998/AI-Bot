from hazm import *
from parsivar import POSTagger


#Correcting the github account
#Now my account works correctly it's compeltely ok


stopwords=stopwords_list("Persian_stopwords.txt")
sent='فردا هوای تهران و شیراز چند درجه  خواهد شد؟'
print(sent)
normalizer = Normalizer()
sen=normalizer.normalize(sent)
print(sen)
token=word_tokenize(sen)
print(token)
sentence=[]
for w in token:
    if w not in stopwords:
        sentence.append(w)

lema=[]
for w in sentence:
    lema.append(Lemmatizer().lemmatize(w))
print("lemetizer:", lema)
#Label the lemetized words with Part of Speech(POS)

tagger=POSTagger(tagging_model="wipti")
tag=tagger.parse(lema)
print("POStag:", tag)

#Noun is a list variable which save the names in the sentence
noun=[]
for x in tag:
    if x[1]=="N":
        noun.append(x)
print("Noun:",noun)

#Do the former part for the ADJ
ADV=[]
for x in tag:
    if x[1]=="ADV":
        ADV.append(x)
print("ADV:",ADV)

#lemetizing the tokens
