# import nltk packages
import nltk
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
from part_of_speech import get_part_of_speech
from nltk.corpus import wordnet as wn
import re
nltk.download('averaged_perceptron_tagger')


lemmatizer = WordNetLemmatizer()

main_title = input("ENTER TITLE: ")



def antonyms_for(word):
    antonyms = set()
    for ss in wn.synsets(word):
        for lemma in ss.lemmas():
            any_pos_antonyms = [ antonym.name() for antonym in lemma.antonyms() ]
            for antonym in any_pos_antonyms:
                antonym_synsets = wn.synsets(antonym)
                if wn.ADJ not in [ ss.pos() for ss in antonym_synsets ]:
                    continue
                antonyms.add(antonym)
    return antonyms

def re_indent_adj(sentence):
    tags = nltk.pos_tag(sentence.split(' '))
    adjectives = list
    adjectives = [w for w, t in tags if t == 'JJ']

    tokenized_title = word_tokenize(sentence)
    #print(tokenized_title)
    value = 0
    for i in adjectives:
        current_adj = (adjectives[value])
        print(antonyms_for(current_adj))
        if antonyms_for(current_adj) == set():
            return("Sorry we are not able to find a antoym sentence")
        else:
            adj_position = tokenized_title.index(current_adj)
            #print(adj_position)
            tokenized_title[adj_position] = (antonyms_for(current_adj).pop())
            tokenized_title_str = " ".join(map(str, tokenized_title))
            #print(tokenized_title_str)
            return(tokenized_title_str)
        value += 1



print(re_indent_adj(main_title))
