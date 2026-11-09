# Algoritmos para la vida diaria

> Publicado en LinkedIn el [22 de diciembre de 2023](https://www.linkedin.com/feed/update/urn:li:activity:7143972905163403264/).

Los algoritmos son mucho más que marcos para resolver problemas matemáticos; son marcos/paradigmas que te ayudan a navegar y resolver los problemas que surgen en tu vida diaria.

Me gusta bromear con que vivo mi vida como si fuera un problema de optimización multiescala, multiobjetivo y estocástico :)

Por ejemplo, me gusta pensar en escribir un artículo desde la perspectiva de un paradigma algorítmico llamado "multimalla" (multigrid), muy usado para resolver problemas multiescala. La idea es construir una jerarquía de representaciones de un sistema, cada una capturando características a distintas escalas; en la figura original se ve lo más fino arriba y lo más grueso abajo, pero también puedes invertir el orden, con lo grueso arriba y lo fino abajo (prefiero esta visión).

Puedes encontrar una solución del nivel superior que capture las características gruesas del problema (que te dé el esqueleto, por así decirlo) y luego pasar esa solución a un problema de nivel inferior que busca corregir detalles/defectos. En el nivel inferior, puedes descomponer el sistema en subdominios y refinar cada uno de forma progresiva (iterando sobre cada subdominio, y puedes refinarlo recorriendo los subdominios en distinto orden).

Escribir un artículo se siente justo así: puedes empezar escribiendo un esqueleto/andamio de todo sin capturar los detalles finos. Una vez que tienes el esqueleto, saltas a distintos subdominios/secciones y los refinas; puedes iterar sobre las secciones en distinto orden (por ejemplo, del inicio al final o del final al inicio). La observación interesante que te deja el método multimalla es que, si empiezas a iterar sobre las subsecciones sin tener un esqueleto, vas a converger a una solución (por ejemplo, a una historia coherente), pero vas a converger lentamente... por eso es importante tener un esqueleto que capture los aspectos generales de la historia. También puedes decidir tener varios niveles de resolución; esto se vuelve particularmente importante en proyectos grandes, como escribir una tesis o un libro.

Lo que me gusta del marco multimalla es que hay muchas maneras de diseñarlo, según tus metas o el problema en cuestión. En general, es simplemente un marco conveniente para descomponer proyectos grandes (por ejemplo, en carpintería y construcción).

Disfruto encontrar aplicaciones de los algoritmos en la vida real; hace unos años leí este libro ("Algorithms to Live By", de Christian y Griffiths; en español, "Algoritmos para vivir"), que recomiendo mucho: https://lnkd.in/gVQhQRUQ

En general, creo que tratar de encontrar aplicaciones de los algoritmos con los que trabajas puede ser divertido y también te ayuda a desarrollar tus habilidades de abstracción.

Crédito de la figura: https://lnkd.in/gBHC5A6r

:::{note}
La publicación original incluía un diagrama del método multimalla que no se reproduce aquí. Puedes verlo en la publicación de LinkedIn.
:::
