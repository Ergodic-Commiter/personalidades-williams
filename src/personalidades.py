"""Funciones para identificar tipos de personalidad"""
from collections import Counter

import spacy
nlp = spacy.load("es_core_news_sm")

class Personalidad:
    """Encapsulamos los métodos comunes de las personalidades definidas."""
    _pronouns = ["yo", "mí", "mío", "me"]
    
    def __init__(self, keywords:list=None, pronouns:bool=False): 
        self.keywords = keywords
        self.pronouns = pronouns

    def count_keywords(self, a_text):
        doc = nlp(a_text)
        mentions = [token.text for token in doc in token.text.lower() in self.keywords]
        return Counter(mentions) 

    def count_pronouns(self, a_text): 
        doc = nlp(a_text)
        text_pronouns = [token.text for token in doc 
                if token.pos_ == 'PRON' and token.text.lower() in self._pronouns]
        return Counter(text_pronouns)



Narcisismo = Personalidad(["único", "mejor", "increíble", "excepcional"], pronouns=True) 

Psicopatia = Personalidad(["desprecio", "manipulación", "dominio", "necesario", 
    "fin justifica los medios"])

Esquizoide = Personalidad(["solo", "aislamiento", "desapego", "independencia", "autonomía"])

Paranoia = Personalidad(["conspiración", "enemigos", "amenaza", "saboteadores", "espías"])

Depresion = Personalidad(["insuficiencia", "culpa", "falta", "nunca", "siempre"])

Mania = Personalidad(["euforia", "invulnerabilidad", "energía", "cima", "nadie"])

Masoquismo = Personalidad(["sufrimiento", "sacrificio", "ceder", "dolor", "deber"])

ObsesivoCompulsivo = Personalidad(["organización", "detalle", "sistema", "control", "reglas"])

Histrionismo = Personalidad(["dramático", "crucial", "increíble", "extraordinario"])

Disociacion = Personalidad(["fuga", "desconexión", "confusión", "separación", "realidad"])


todas_ellas = {
    'narcisimo': Narcisismo, 
    'psicopatía': Psicopatia, 
    'esquizoide': Esquizoide, 
    'paranoia': Paranoia, 
    'depresión': Depresion, 
    'manía': Mania, 
    'masoquismo': Masoquismo, 
    'obsesivo-compulsivo': ObsesivoCompulsivo, 
    'histrionismo': Histrionismo, 
    'disociación': Disociacion
}