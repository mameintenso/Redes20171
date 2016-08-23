# Redes 2017-1

Repositorio creado para almacenar las prácticas del curso de Redes de Computadoras
de la Facultad de Ciencias de la UNAM, durante el semestre 2017-1.

**Autores:**

* [Albert Manuel Orozco Camacho](http://github.com/AlOrozco53)
* [Erick Iván Pérez Jiménez](http://github.com/TuringOraculosLocos)

# Reporte de la práctica 2

* Define el concepto de procedimientos remotos.
  ** Son aquellos procedimientos que se ejecutan de una computadora a otra, es decir que envian información
  de un puerto de una computadora, al puerto de otra.

* ¿Qué es una IP y para qué sirve?
 ** La IP es un identificador perteneciente al protocolo de Internet, el cual se usa actualmente
 en su cuarta versión. Se trata de una manera de identificar de manera única a una computadora
 dentro de una red, es decir, es como la __dirección postal__ de un sistema de cómputo dentro del Internet,
 haciendo una analogía con una mensajería de correos.

* A grandes rasgos define lo que es un puerto.
  ** Un puerto es el espacio de entrada y salida que se le asigna a un proceso para que pueda
  utilizar servicios de red.

*¿Se puede tener dos clientes en una misma computadora? Es decir, abrir una terminal y correr una
 instancia para Alice, y abrir otra terminal para correr una instancia para Bob y que estos se puedan
 comunicar.
 **Si, si se puede, lo único que necesitas es usar un puerto diferente para cada cliente.
 
 *Particularidades del código
  * Cual es el flujo del problema y para que sirve cada archivo dentro de la carpeta GUI y Channel
    ** En la carpeta del GUI se encuentra la interfaz gráfica de la ventana de selección de puertos
    y en la otra se encuentra la ventana gráfica del chat, en la parte de Channel está el servidor, el cliente 
    y el manejo de los threads. El flujo del problema consiste en abrir dos terminales, cada una lenvanta su
    cliente y su servidor y cada cliente se comunica con el servidor del otro
  * Principales problemas que se encontraron y cómo los solucionaron.
    ** Tuvimos problemas con hacer que la caja donde se escribía el texto se quedara guardada en el widget de
    historial.
  * Problemas que no fueron solucionados
    ** Al parecer todo funciona bien.
