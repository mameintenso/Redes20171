# Redes 2017-1

## Práctica 4

**Autores:**

* [Albert Manuel Orozco Camacho](http://github.com/AlOrozco53)
* [Erick Iván Pérez Jiménez](http://github.com/TuringOraculosLocos)

# Reporte de la práctica 4

### ¿Qué pasa si la red esporádicamente pierde paquetes, cómo afectaría esto al audio y al video?
Si se pierden paquetes, el programa debería de seguir corriendo hasta que el usuario mande terminar los
hilos que ejecutan al audio y/o video. Entonces por algunos instantes, el audio se dejaría de escuchar y
el video se congelaría.

### Respecto a la pregunta anterior, ¿cómo afecta esta situación al desempeño de la red?
Una de las causas de pérdida de paquetes es el aumento de la [latencia] (nivel de tráfico) en la red.
Dada la naturaleza de las tareas de transmición de audio y video, es posible que si al intentar reenviar
un paquete, se pierdan muchos más que van llegando, ya que al grabar se generan muchos paquetes por unidad
de tiempo. Por ello, si la pérdida de paquetes no afecta en gran medida la comunicación entre un usuario y otro,
es posible ignorarla.

### ¿Qué solución puede darse para evitar los problemas de las preguntas anteriores, y en que capa del modelo osi suele resolverse ?
Para éste tipo de aplicaciones se suele usar UDP en vez de TCP, ya que, como se vio en la pregunta anterior,
se puede ignorar la retransmisión de paquetes perdidos si es que la pérdida de los mismos no es significativa. Por tanto,
la solución al problema se implementa en la capa de transporte.

Cabe destacar que el en programa sólo se probó para el uso en la misma máquina y NO se puede mandar audio o video
al mismo tiempo :(.