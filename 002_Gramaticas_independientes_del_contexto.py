import nltk
from nltk import CFG
from nltk.parse.generate import generate

# Define una gramática independiente del contexto (CFG) simple
grammar = CFG.fromstring("""
    S -> NP VP
    NP -> Det N
    VP -> V NP
    Det -> 'the' | 'a'
    N -> 'cat' | 'dog' | 'ball'
    V -> 'chased' | 'ate'
""")

# Genera y muestra algunas frases válidas según la CFG
for sentence in generate(grammar, n=5):
    print(' '.join(sentence))

# Definir un analizador probabilístico utilizando CFG y PCFG
from nltk.corpus import treebank
from nltk import PCFG
from nltk.grammar import induce_pcfg

# Cargar el corpus de Treebank
corpus = treebank.parsed_sents()

# Inducir una gramática probabilística (PCFG) a partir del corpus
pcfg_grammar = induce_pcfg(PCFG, corpus)

# Mostrar una producción y su probabilidad
production = pcfg_grammar.productions()[0]
print(f"Producción: {production}")
print(f"Probabilidad: {pcfg_grammar.productions()[0].prob()}")
