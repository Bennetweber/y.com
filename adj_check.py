import nltk
nltk.download('averaged_perceptron_tagger')

sentence = input("ENTER: ")
tags = nltk.pos_tag(sentence.split(' '))
adjectives = [w for w, t in tags if t == 'JJ']
print(adjectives)
