# nsfw_image_detection_API
Esta aplicación Flask proporciona una interfaz sencilla para clasificar imágenes como "seguras" o "no seguras para el trabajo" (NSFW) utilizando una API de Hugging Face. El código incluye las siguientes características y funcionalidades:

1. **Configuración Inicial**: Se importan las bibliotecas necesarias y se configura la aplicación Flask. También se define la URL de la API y los encabezados de autenticación para conectarse al modelo de Hugging Face que realiza la detección de imágenes NSFW.

2. **Funciones de Utilidad**:
   - `query(file)`: Esta función envía la imagen a la API de Hugging Face y retorna la respuesta JSON.
   - `get_highest_score_label(response_json)`: Extrae la etiqueta con el mayor puntaje de la respuesta JSON, lo cual indica la clasificación de la imagen.

3. **Rutas de Flask**:
   - La ruta `'/'` carga la página principal donde los usuarios pueden subir imágenes.
   - La ruta `'/upload'`, que maneja POST, permite a los usuarios subir un archivo. Si el archivo es válido, se clasifica mediante la función `query`, se almacena temporalmente en una carpeta de subidas y se retorna la clasificación junto con la ruta del archivo guardado.

4. **Manejo de Errores**: Se proporcionan respuestas JSON informativas en caso de que ocurran errores, como la falta de un archivo en la petición o un error interno.

5. **Ejecución y Configuración del Servidor**: Al final del archivo, se asegura que la carpeta de subidas exista y se inicia la aplicación en modo de depuración.

Este código puede ser particularmente útil para plataformas que necesitan pre-moderar contenido visual para asegurar que no contenga material inapropiado, ofreciendo una solución automatizada y eficiente para la moderación de contenido en tiempo real. Puedes describir este proyecto en tu repositorio de GitHub como una herramienta de moderación de contenido basada en inteligencia artificial que integra tecnologías avanzadas de clasificación de imágenes.
