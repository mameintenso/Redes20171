# Redes 2017-1

## Práctica 1

**Autores:**

* [Albert Manuel Orozco Camacho](http://github.com/AlOrozco53)
  * __41308026-0__
* [Erick Iván Pérez Jiménez](http://github.com/TuringOraculosLocos)
  * __núm-cta-ñérick__

En esta rama se implementó un servicio de dos calculadoras simples.

El usuario debe darse de alta con un nombre de usuario y una contraseña que
se guardan en el archivo Code/Input.txt de manera cifrada. Dicho archivo
guarda un usuario por línea separando el nombre de usuario cifrado de la contraseña
cifrada por un espacio; por ejemplo:

usr1 psswd1
usr2 psswd2
.
.
.
usrn psswdn

El cifrado es de tipo _César_ con un _offset_ de 5 unidades en el subconjunto del
alfabeto ASCII que incluyen a todos los carácteres visibles en el teclado. Es decir,
del carácter 33 al 126, inclusivo. Por ello, se recomienda que el usuario
construya sus credenciales mediante carácteres alfanuméricos. Todo lo anterior
está escrito en Code/DataBase.py.

En Constants/Constants.py están todas las constantes que el programa necesita
para no usar números mágicos.

En Code/Calculator.py están definidas las dos calculadoras. La más simple
sólo realiza sumas y restas y la avanzada puede dividir y multiplicar.

Las calculadoras SÓLO se pueden usar haciendo clic en los botones.

La práctica se realizó en Python 3.5