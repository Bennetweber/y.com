from nltk.corpus import wordnet as wn


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

words_set = antonyms_for("bad")
if words_set:
   first_word = list(words_set)[0]
   print(f'first antonym: {first_word}')  # expected to print 'unregretful'
else:
   print('No antonym found!')


print(antonyms_for("bad").pop())
