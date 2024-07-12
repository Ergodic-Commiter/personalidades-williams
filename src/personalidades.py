"""Funciones para identificar tipos de personalidad"""
from collections import Counter

import spacy
nlp = spacy.load("es_core_news_sm")


class Personalidad:
    """Encapsulamos los métodos comunes de las personalidades definidas."""
    _pronombres = ["yo", "mí", "mío", "me"]
    
    def __init__(self, palabras_claves:list=None, pronombres:bool=False): 
        self.p_claves = palabras_claves
        self.pronombres = pronombres

    def identificame(self, un_texto):
        doc = nlp(un_texto)
        menciones = [token.text for token in doc 
                if token.text.lower() in self.p_claves]        
        if not self.pronombres: 
            return Count(menciones)
        return self.cuenta_pronombres(un_texto), Count(menciones)

    def cuenta_pronombres(self, un_texto): 
        doc = nlp(un_texto)
        y_pronombres = [token.text for token in doc 
                if token.pos_ == 'PRON' and token.text.lower() in self._pronombres]
        return Counter(y_pronombres)


Narcisismo = Personalidad(["único", "mejor", "increíble", "excepcional"], pronombres=True) 

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