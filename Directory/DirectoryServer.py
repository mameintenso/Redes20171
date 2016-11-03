#! /usr/bin/env python
# -*- coding: utf-8 -*-


#####################################################
# PURPOSE: Clase que manejara los clientes que se   #
#          conectan y desconectan al sistema        #
#                                                   #
# Vilchis Dominguez Miguel Alonso                   #
#       <mvilchis@ciencias.unam.mx>                 #
#                                                   #
# Notes:                                            #
#                                                   #
# Copyright   17-08-2015                            #
#                                                   #
# Distributed under terms of the MIT license.       #
#####################################################
from SimpleXMLRPCServer import SimpleXMLRPCServer
from SimpleXMLRPCServer import SimpleXMLRPCRequestHandler

# Mis bibliotecas
import sys,getopt
sys.path.insert(0, '../')
sys.path.insert(0, 'Constants')
from AuxiliarFunctions import *
from Constants import *
# Restrict to a particular path.
class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

class GeneralDirectory:

    def __init__(self, port=None):
        """ Constructor de la clase, si recibe un puerto, entonces
        trabajará de manera local, de otra manera, utilizará  la ip
        con la que cuenta.
        @param port <int> Si trabaja de manera local, representa el
        número del puerto por el cual recibirá las peticiones
        """
        self.client_dictionary = {}
        functionWrapper = FunctionWrapperDirectory(self.client_dictionary)
        ip = get_ip_address()
        if port is None:
            self.port = SERVER_PORT
            self.my_ip = ip
        else:
            self.port = port
            self.my_ip = 'localhost'
        self.server = SimpleXMLRPCServer((self.my_ip, int(self.port)),
                                         requestHandler=RequestHandler,
                                         allow_none=True)
        self.server.register_instance(functionWrapper)
        print "Directorio de ubicacion activo, mi dirección es:"
        print "(%s, %s)" %(self.my_ip, self.port)


class FunctionWrapperDirectory:
    """ **************************************************
    Constructor de la clase
    @clients_dictionary (Diccionario) Contiene la información de
                todos los clientes (Usa username como llave, y contiene el nombre del usuario)
    ************************************************** """
    def __init__(self, client_dictionary):
        self.client_dictionary = client_dictionary


    def get_contacts_wrapper(self, username):
        contacts_dict = {}
        for k, v in self.client_dictionary.iteritems():
            if k != username:
                contacts_dict[k] = v
        return contacts_dict

    def connect_wrapper(self, ip_string, port_string, username):
        if username in self.client_dictionary.keys():
            raise KeyError('Username already taken!')
        else:
            self.client_dictionary[username] = {IP_CONTACT: ip_string,
                                                PORT_CONTACT: port_string,
                                                NAME_CONTACT: username}
            print 'successfully added entry\n' +\
                str(self.client_dictionary[username]) + '\n' +\
                'with key: ' + str(username) + '\n--------'

    def disconnect_wrapper(self, username):
        if username in self.client_dictionary.keys():
            del self.client_dictionary[username]
            print 'user ' + username + ' just logged-out successfully!'

# **************************************************
#  Definicion de la funcion principal
#**************************************************
def error_message():
    print 'Uso con puertos locales:'
    print '$ python Directory/DirectoryServer.py -l <puerto>'
    print 'Uso entre computadoras dentro de la red'
    print '$ python Directory/DirectoryServer.py '
    sys.exit(2)

def main(argv):
    try:
        opts, args = getopt.getopt(argv, "l", ["local="])
        if opts: #Si el usuario mandó alguna bandera
            local = True if '-l' in opts[0] else False
        else:
            local = False
        if local:
            general_server = GeneralDirectory(port=args[0]).server
        else:
            general_server = GeneralDirectory().server
    except:
        error_message()
    general_server.serve_forever()


if __name__ == '__main__':
    main(sys.argv[1:])
