#! /usr/bin/env python
# -*- coding: utf-8 -*-

from Channel.ApiClient import *
from Channel.ApiServer import *

"""
Las instancias de esta clase contendran los metodos
necesarios para hacer uso de los metodos
del api de un contacto. Internamente Trabajara
con una proxy apuntando hacia los servicios del
servidor xmlrpc del contacto
"""
class Channel:

    def __init__(self, local_ip, local_port, contact_ip, contact_port, gui):
        """
        Constructor de la clase
        @param <str> contact_ip: Si no se trabaja de manera local
        representa la ip del contacto con el que se
        establecera la conexion
        @param <int> my_port: De trabajar de manera local puerto
        de la instancia del cliente
        @param <int> contact_port: De trabajar de manera local
        representa el puerto de la instancia del contacto
        """
        self.proxy_uri = 'http://' + contact_ip + ':' + contact_port
        self.my_ip = local_ip
        self.my_port = local_port
        self.api_server = MyApiServer(self.my_ip, self.my_port, gui)
        self.api_client = MyApiClient(self.proxy_uri)

        # start server
        self.api_server.start()


    def send_text(self, text):
        """
        Metodo que se encarga de mandar texto al contacto con
        el cual se estableció la conexion
        """
        print(self.api_client.send_message(text))

# if __name__ == '__main__':
#     cont_ip = input('give me a contact ip: ')
#     cont_port = input('give me a contact port: ')
#     channel = Channel(cont_ip, cont_port)
#     while True:
#         try:
#             mess = input('>> ')
#             channel.send_text(mess)
#         except KeyboardInterrupt:
#             print("\nKeyboard interrupt received, exiting.")
#             self.server.server_close()
#             sys.exit(0)
