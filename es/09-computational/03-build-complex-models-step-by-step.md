# Construye los modelos complejos paso a paso

> Publicado en LinkedIn el [21 de septiembre de 2023](https://www.linkedin.com/feed/update/urn:li:activity:7110432672971165696/).

Al implementar un modelo muy complejo, es importante desarrollar una estrategia para construirlo, depurarlo y validarlo de forma *progresiva*.

Empieza sencillo; implementa un modelo mínimo que capture algunas de las características iniciales de tu problema. Haz las suposiciones necesarias (por ejemplo, comportamiento lineal, estado estacionario, ignorar restricciones) para obtener resultados que esperas.

Una vez que tu modelo inicial dé el comportamiento esperado, empieza a agregar características de forma progresiva, y hazlo de manera que puedas aislar los efectos. Trata de no dar saltos bruscos en la complejidad del modelo (da pasos pequeños) y valida el comportamiento en cada paso.

Evita implementar primero el modelo complejo completo; eso es buscarse problemas. Muchas cosas pueden salir (y saldrán) mal al implementar y ejecutar un modelo, y será difícil identificar los problemas si empiezas con el modelo complejo. Por ejemplo, necesitas separar los problemas asociados a las características del modelo de los problemas numéricos.

Además, al construir tu modelo de forma progresiva, aprenderás más sobre el comportamiento del sistema y sobre los aspectos que influyen en ese comportamiento. También es mucho más fácil experimentar con modelos simples que con modelos complejos.

En general, siento que una habilidad esencial para lidiar con la complejidad es construir y analizar las cosas de forma modular. Para hacerlo, necesitas encontrar maneras de crear "sustitutos" con distintos niveles de complejidad. Es una habilidad muy útil en el desarrollo de modelos (y en la ciencia en general).
