import nltk

# Definir una gramática PCFG
grammar = nltk.PCFG.fromstring("""
    S -> NP VP [1.0]
    NP -> Det N [0.6] | Det N PP [0.4]
    VP -> V [0.3] | V NP [0.7]
    PP -> P NP [1.0]
    Det -> 'the' [1.0]
    N -> 'cat' [0.3] | 'dog' [0.4] | 'bird' [0.3]
    V -> 'chased' [0.5] | 'saw' [0.5]
    P -> 'in' [0.6] | 'on' [0.4]
""")

# Crear un analizador sintáctico probabilístico
parser = nltk.ViterbiParser(grammar)

# Analizar una oración
sentence = "the cat chased the dog on the mat"
tokens = sentence.split()
parsed_trees = list(parser.parse(tokens))

# Mostrar los árboles de análisis probabilísticos
for tree in parsed_trees:
    print("Árbol de análisis:", tree)
    tree.pretty_print()
    print("Probabilidad:", tree.prob())
