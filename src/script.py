
from datetime import datetime
import os
import re

from gensim import corpora, models
import matplotlib.pyplot as plt
import pandas as pd
import PyPDF2
from textblob import TextBlob
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from nltk.corpus import stopwords
from wordcloud import WordCloud

from personalidades import todas_ellas
# Configurar la ruta de los discursos

# folder_path = "C:\\Users\\Rodolfo Franco\\OneDrive\\Desktop\\Discursos AMLO"

# Función para leer archivos PDF y extraer texto y fecha
def leer_discursos(folder_path):
    discursos = []
    archivos = sorted(os.listdir(folder_path))  # Ordenar archivos por nombre
    for i, file_name in enumerate(archivos):
        if file_name.endswith(".pdf"):
            file_path = os.path.join(folder_path, file_name)
            with open(file_path, 'rb') as file:
                reader = PyPDF2.PdfReader(file)
                texto = ""
                for page in reader.pages:
                    if page.extract_text():
                        texto += page.extract_text()
                # Limpiar el texto extraído de caracteres no permitidos
                texto = limpiar_texto(texto)
                # Extraer fecha del nombre del archivo
                fecha = extraer_fecha(file_name)
                if not fecha:
                    fecha = calcular_fecha_promedio(archivos, i)
                discursos.append({'texto': texto, 'fecha': fecha})
    return discursos

# Función para extraer la fecha del nombre del archivo
def extraer_fecha(file_name):
    match = re.search(r'\d{4}-\d{2}-\d{2}', file_name)
    if match:
        return datetime.strptime(match.group(), '%Y-%m-%d').date()
    return None

# Función para calcular la fecha promedio entre el archivo anterior y el siguiente
def calcular_fecha_promedio(archivos, index):
    fechas = []
    
    # Obtener la fecha del archivo anterior
    if index > 0:
        fecha_anterior = extraer_fecha(archivos[index - 1])
        if fecha_anterior:
            fechas.append(fecha_anterior)
    
    # Obtener la fecha del archivo siguiente
    if index < len(archivos) - 1:
        fecha_siguiente = extraer_fecha(archivos[index + 1])
        if fecha_siguiente:
            fechas.append(fecha_siguiente)
    
    if len(fechas) == 2:
        fecha_promedio = fechas[0] + (fechas[1] - fechas[0]) / 2
        return fecha_promedio.date()
    elif len(fechas) == 1:
        return fechas[0]
    else:
        # Si no se encuentra una fecha válida, asignar una fecha por defecto
        return datetime.today().date()

# Función para limpiar texto de caracteres no permitidos
def limpiar_texto(texto):
    return re.sub(r'[^\x00-\x7F]+', ' ', texto)


# Función para preprocesar el texto
def preprocesar_texto(texto):
    texto = re.sub(r'\s+', ' ', texto)
    texto = re.sub(r'[^\w\s]', '', texto)
    texto = texto.lower()
    return texto

# Función para análisis de sentimientos con TextBlob y VADER
def analizar_sentimientos(texto):
    blob = TextBlob(texto)
    vader = SentimentIntensityAnalyzer()
    sentiment_textblob = blob.sentiment.polarity
    sentiment_vader = vader.polarity_scores(texto)
    return sentiment_textblob, sentiment_vader

# Función para modelado de temas con Gensim
def modelar_temas(discursos_procesados, num_temas=5):
    textos = [doc.split() for doc in discursos_procesados]
    diccionario = corpora.Dictionary(textos)
    corpus = [diccionario.doc2bow(texto) for texto in textos]
    modelo_lda = models.LdaModel(corpus, num_topics=num_temas, id2word=diccionario, passes=15)
    return modelo_lda.print_topics(num_words=5)
    

#

# Función para generar nubes de palabras
def generar_nube_palabras(texto, titulo):
    wordcloud = WordCloud(stopwords=stopwords.words('spanish'),
                          background_color='white',
                          width=800, height=400).generate(texto)
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.title(titulo)
    plt.show()

# Función para guardar datos en CSV
def guardar_en_csv(datos, nombre_archivo):
    df = pd.DataFrame(datos)
    df.to_csv(nombre_archivo, index=False, encoding='utf-8-sig')

# Función para guardar datos en JSON
def guardar_en_json(datos, nombre_archivo):
    df = pd.DataFrame(datos)
    df.to_json(nombre_archivo, orient='records', lines=True, force_ascii=False)

# Leer y preprocesar discursos
discursos = leer_discursos(folder_path)
discursos_procesados = [{'texto': preprocesar_texto(disc['texto']), 'fecha': disc['fecha']} 
    for disc in discursos]

# Análisis de sentimientos
resultados_sentimientos = []
for discurso in discursos_procesados:
    sentiment_textblob, sentiment_vader = analizar_sentimientos(discurso['texto'])
    resultados_sentimientos.append({
        'fecha': discurso['fecha'],
        'sentiment_textblob': sentiment_textblob,
        'sentiment_vader': sentiment_vader
    })

# Modelado de temas
temas = modelar_temas([disc['texto'] for disc in discursos_procesados])

# Detección de tipos de personalidad
resultados_personalidades = []
for discurso in discursos_procesados:
    texto = discurso['texto']
    fecha = discurso['fecha']

    psicopatia = identificar_psicopatia(texto)
    narcisismo = identificar_narcisismo(texto)
    esquizoide = identificar_esquizoide(texto)
    paranoia = identificar_paranoia(texto)
    depresion = identificar_depresion(texto)
    mania = identificar_mania(texto)
    masoquismo = identificar_masoquismo(texto)
    ocd = identificar_ocd(texto)
    histrionismo = identificar_histrionismo(texto)
    disociacion = identificar_disociacion(texto)
    
    resultados_personalidades.append({
        'fecha': fecha,
        'psicopatia': psicopatia,
        'narcisismo': narcisismo,
        'esquizoide': esquizoide,
        'paranoia': paranoia,
        'depresion': depresion,
        'mania': mania,
        'masoquismo': masoquismo,
        'ocd': ocd,
        'histrionismo': histrionismo,
        'disociacion': disociacion
    })

# Guardar resultados en CSV y JSON
guardar_en_csv(resultados_sentimientos, 'sentimientos.csv')
guardar_en_csv(resultados_personalidades, 'personalidades.csv')

guardar_en_json(resultados_sentimientos, 'sentimientos.json')
guardar_en_json(resultados_personalidades, 'personalidades.json')

# Imprimir algunos resultados
print("\nResultados de Personalidades:")
for resultado in resultados_personalidades:
    print(f"Fecha: {resultado['fecha']}")
    print(f"Psicopatia: {resultado['psicopatia']}")
    print(f"Narcisismo: {resultado['narcisismo']}")
    print(f"Esquizoide: {resultado['esquizoide']}")
    print(f"Paranoia: {resultado['paranoia']}")
    print(f"Depresion: {resultado['depresion']}")
    print(f"Mania: {resultado['mania']}")
    print(f"Masoquismo: {resultado['masoquismo']}")
    print(f"OCD: {resultado['ocd']}")
    print(f"Histrionismo: {resultado['histrionismo']}")
    print(f"Disociacion: {resultado['disociacion']}")

# Generar nube de palabras para todos los discursos
todos_discursos = ' '.join([disc['texto'] for disc in discursos_procesados])
generar_nube_palabras(todos_discursos, 'Nube de Palabras de Todos los Discursos')

# Imprimir análisis de sentimientos
print("\nAnálisis de sentimientos (TextBlob y VADER):")
for resultado in resultados_sentimientos:
    print(f"Fecha: {resultado['fecha']}, TextBlob: {resultado['sentiment_textblob']}, VADER: {resultado['sentiment_vader']}")

# Imprimir temas
print("\nTemas encontrados:")
for tema in temas:
    print(tema)