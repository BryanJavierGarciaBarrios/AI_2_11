import spacy

# Cargar el modelo en español de spaCy
nlp = spacy.load("es_core_news_sm")

# Texto de ejemplo
text = "El presidente de Estados Unidos, Joe Biden, se reunió con la canciller alemana, Angela Merkel, en Washington."

# Procesar el texto
doc = nlp(text)

# Extraer información
entities = {}
relations = []

for ent in doc.ents:
    entities[ent.text] = ent.label_

for token in doc:
    if "presidente" in token.text and "canciller" in token.text:
        relations.append((token.text, "y", "se reunió con"))

# Imprimir resultados
print("Entidades identificadas:")
for entity, label in entities.items():
    print(f"{entity} ({label})")

print("\nRelaciones identificadas:")
for relation in relations:
    print(f"{relation[0]} {relation[1]} {relation[2]}")

