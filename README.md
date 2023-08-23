# DetectorEmociones
Detecta lo que se le dice y calcula la emoción, devolviéndonos si es positivo, negativo o neutro.

Readme para la Aplicación de Análisis de Sentimientos con GPT-3
Este es un sencillo programa de análisis de sentimientos que utiliza la API de OpenAI y se ejecuta en Python. Su función es permitir a los usuarios ingresar mensajes y recibir respuestas que representen el sentimiento de esos mensajes.

Requisitos Previos
Asegúrate de tener los siguientes requisitos previos antes de utilizar esta aplicación:

Python: Debes tener Python instalado en tu sistema. Puedes descargarlo desde python.org si aún no lo tienes.

PIP: Debes tener PIP (Python Package Installer) instalado. PIP se instala automáticamente con Python en versiones recientes. Puedes verificar si tienes PIP ejecutando pip --version en tu terminal.

Configuración
Clave de API de OpenAI: Debes obtener una clave de API de OpenAI desde su plataforma. Reemplaza "..." en el código con tu clave de API.
Uso
Para utilizar esta aplicación, sigue estos pasos:

Ejecuta el script Python en tu terminal:

python nombre_del_script.py
Reemplaza nombre_del_script.py con el nombre de tu archivo Python.

La aplicación se iniciará y te pedirá que ingreses un mensaje. Ingresa el mensaje y presiona Enter.

La aplicación enviará el mensaje a la API de OpenAI y recibirá una respuesta que representa el sentimiento del mensaje.

La respuesta se mostrará en la terminal junto con un código de color que indica el sentimiento. Por ejemplo, "Muy Positivo" se mostrará en verde, "Negativo" en rojo, etc.

Puedes seguir ingresando mensajes y recibiendo respuestas mientras mantengas la aplicación en ejecución.

Acerca de los Sentimientos
El programa utiliza una escala de sentimientos que va desde -1 (negatividad máxima) a 1 (positividad máxima), con 0 siendo neutral. Puedes interpretar los valores entre estos extremos como sentimientos en diferentes grados de positividad o negatividad.

Personalización
Si deseas personalizar los rangos de sentimientos o los colores utilizados para representarlos, puedes hacerlo modificando el código en la sección "Configuración".

Limitaciones
Ten en cuenta que esta es una aplicación de demostración y que la precisión de los resultados del análisis de sentimientos puede variar. Si deseas un análisis de sentimientos más avanzado o específico, considera utilizar herramientas y bibliotecas de procesamiento de lenguaje natural más especializadas.

Créditos
Este programa utiliza la API de OpenAI y la biblioteca Colorama para la representación de colores en la terminal.

Espero que encuentres esta aplicación útil para explorar y comprender el análisis de sentimientos. ¡Diviértete experimentando con ella!




