### Integración del Análisis Psicoanalítico en el Script

Para integrar el análisis psicoanalítico basado en los tipos de personalidad descritos 
por Nancy McWilliams en el script de análisis de discursos de AMLO, agregaremos 
funciones para identificar características de cada tipo de personalidad en los discursos. 
Cada función analizará el texto en busca de palabras clave y patrones específicos 
relacionados con cada tipo de personalidad.

### Instalación de Librerías Necesarias

0. Instalar `conda` y `git`  
  Uno se descarga [de este link][anaconda]  
  El otro se ejecuta en terminal: 
  ```shell
  $ sudo apt install git
  ```
  
1. Clonar repo en computadora: 
  ```shell
  $ git clone REPO_URL {nombre-local}
  ```

2. Crear ambiente de Anaconda (se tarda un buen rato 😒) 
  ```shell
  $ conda env create -f conda.yml
  ```  

  El ambiente te descarga las librerías de manera local. 

3. Adicionalmente descargar las noticias con `spacy`
  ```
  python -m spacy download es_core_news_sm
  ```

4. El _script_ lo guardamos en la carpeta `src` para organizarlo y ampliarlo. 

[anaconda]: https://anaconda.org