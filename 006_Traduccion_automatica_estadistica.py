import nltk
import random

# Descargar los datos necesarios para NLTK (corpus y modelos)
nltk.download('punkt')
nltk.download('reuters')

from nltk import bigrams
from nltk.corpus import reuters
from collections import defaultdict

# Recopilar estadísticas de bigramas de un corpus de ejemplo (Reuters)
def build_bigram_model(corpus):
    bigram_model = defaultdict(lambda: defaultdict(lambda: 0))

    for sentence in corpus.sents():
        for w1, w2 in bigrams(sentence, pad_right=True, pad_left=True):
            bigram_model[w1][w2] += 1

    for w1 in bigram_model:
        total_count = float(sum(bigram_model[w1].values()))
        for w2 in bigram_model[w1]:
            bigram_model[w1][w2] /= total_count

    return bigram_model

# Traducción automática estadística
def translate_sentence(bigram_model, sentence):
    translated_sentence = []

    for w1, w2 in bigrams(sentence, pad_right=True, pad_left=True):
        if w2 is None:
            translated_sentence.append(w1)
            continue

        if w1 in bigram_model and w2 in bigram_model[w1]:
            possible_translations = bigram_model[w1][w2].keys()
            selected_translation = random.choice(possible_translations)
            translated_sentence.append(selected_translation)
        else:
            translated_sentence.append(w1)

    return translated_sentence

# Construir el modelo de bigramas
corpus = reuters
bigram_model = build_bigram_model(corpus)

# Frase de ejemplo para traducir
sample_sentence = ["The", "quick", "brown", "fox"]

# Realizar la traducción
translated_sentence = translate_sentence(bigram_model, sample_sentence)

print("Frase original: ", " ".join(sample_sentence))
print("Frase traducida: ", " ".join(translated_sentence))
