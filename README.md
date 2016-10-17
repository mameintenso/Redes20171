# Redes 2017-1

## Práctica 3

**Autores:**

* [Albert Manuel Orozco Camacho](http://github.com/AlOrozco53)
* [Erick Iván Pérez Jiménez](http://github.com/TuringOraculosLocos)

# Reporte de la práctica 3

**Tu programa funciona bien dentro de la misma red. ¿Si le pasas el proyecto a alguien que se encuentre del otro lado del mundo, podrían comunicarse?**
  No, porque las IPs utilizadas dentro de una red son locales, lo que implica que no son únicas en todo el mundo. Habría que
  enmascarar la IP local con la máscara de red la red local para distinguir a cada computadora de las demás del mundo.

**En el ejemplo anterior ¿Bajo que restricciones podrían comunicarse?**
  Que ambos equipos superan la máscara de red del otro y la IP local.

**Si Alice y Bob están en la misma oficina pero Alice está conectada por ethernet y Bob por wifi. ¿Se pueden comunicar sin problema?
   ¿Bajo qué restricciones se pueden comunicar?**
  Una computadora puede tener más de una IP asignada en una red local debido a que es posible que tenga más de una tarjeta ethernet.
  Por ello, la única restricción sería conocer la IP utilizada para la tarjeta ethernet utilizada en la computadora de Alice.