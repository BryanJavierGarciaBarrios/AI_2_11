import nltk
from nltk.corpus import gutenberg
from nltk.probability import FreqDist
from nltk.tokenize import word_tokenize

# Descargar el corpus de Gutenberg (puede llevar tiempo)
nltk.download('gutenberg')

# Seleccionar un texto específico del corpus de Gutenberg
text = gutenberg.raw('shakespeare-hamlet.txt')

# Tokenizar el texto en palabras
words = word_tokenize(text)

# Calcular la frecuencia de las palabras
fdist = FreqDist(words)

# Ejemplo: Calcular la probabilidad de la palabra "king"
word = "king"
word_probability = fdist.freq(word)

print(f"La probabilidad de la palabra '{word}' es: {word_probability:.4f}")
