# Scrape-Discord-Gpt

Descripcion

Api-Gpt 
![Texto alternativo](Imagenes/Gpt.png)


Scrape Discord Message es una herramienta diseñada para extraer mensajes de Discord y almacenarlos en un formato estructurado. Utiliza la API de Discord y proporciona una interfaz simple para configurar y ejecutar el proceso de scraping. Esta herramienta es útil para analizar datos, realizar estadísticas o realizar copias de seguridad de mensajes en un servidor Discord. Características

Facil Configuracion: Configura tu token de Discord y otros parámetros en un archivo de configuracion sencillo.
Filtrado Avanzado: Personaliza la extracción con opciones de filtrado para obtener solo los mensajes que te interesan.
Exportacion de Datos: Guarda los mensajes en un formato facil de leer, como JSON o CSV, para su analisis posterior.
Interfaz de Linea de Comandos: Ejecuta el scraping desde la linea de comandos con opciones personalizadas.

Uso

El proyecto utiliza Docker para encapsular todas las dependencias necesarias, eliminando as√≠ la necesidad de instalarlas manualmente.


Configuracion del Entorno:
    Clona el repositorio: git clone https://github.com/Christian0221Lopez/Scrape-Discord-Gpt git -b NewPull
    Configura tu token de Discord en config.json.

Ejecutar el Scraping:
    Construye la imagen de Docker: docker build -t scrape-discord .
    Ejecuta el contenedor Docker: docker run -v $(pwd)/output:/app/output scrape-discord

¬°Contribuciones son bienvenidas! Si encuentras errores o deseas mejorar la herramienta, no dudes en abrir un issue o enviar un pull request. Licencia

    Configuraci√≥n del Entorno:
        Clona el repositorio: git clone https://github.com/Christian0221Lopez/Scrape-Discord-Message-Gpt git -b NewPull
        Configura tu token de Discord en config.json.

    Ejecutar el Scraping:
        Construye la imagen de Docker: docker build -t scrape-discord .
        Ejecuta el contenedor Docker: docker run -v $(pwd)/output:/app/output scrape-discord

Los mensajes extraidos se guardar en en un archivo output.json por defecto dentro del directorio output, pero puedes cambiar la configuraci√≥n seg√∫n tus necesidades.
Contribuciones

¬°Contribuciones son bienvenidas! Si encuentras errores o deseas mejorar la herramienta, no dudes en abrir un issue o enviar un pull request.
Licencia

Este proyecto esta bajo la Licencia MIT. Consulta el archivo LICENSE para obtener mas detalles.
