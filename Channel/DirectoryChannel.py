#! /usr/bin/env python
# -*- coding: utf-8 -*-


#####################################################
# PURPOSE: Clase que representa la abstracción de   #
#         Un canal bidireccional (con el servido de #
#         ubicacion), haciendo  uso de la biblioteca#
#         xmlRpc                                    #
#                                                   #
# Vilchis Dominguez Miguel Alonso                   #
#       <mvilchis@ciencias.unam.mx>                 #
#                                                   #
# Notes:                                            #
#                                                   #
# Copyright   16-08-2015                            #
#                                                   #
# Distributed under terms of the MIT license.       #
#####################################################

from ApiServer import *
from Channels import *
from Constants.Constants import CHAT_PORT
from Constants.AuxiliarFunctions import *

class DirectoryChannel(BidirectionalChannel):
    def __init__(self, Qparent, directory_ip=None, my_port=None,
                 directory_port=None, username=None):
        super(DirectoryChannel, self).__init__(Qparent,
                                               contact_ip=directory_ip,
                                               contact_port=directory_port,
                                               my_port=my_port,
                                               my_name=username)
        if directory_ip:
            self.directory_ip = directory_ip
        else:
            self.directory_ip = 'localhost'
        self.my_port = my_port
        self.directory_port = directory_port
        self.username = username

    def get_contacts(self):
        """**************************************************
        Metodo que se encarga de obtener lista de contactos
        **************************************************"""
        self.contact_list = self.api_client.get_contacts(self.username)
        return self.contact_list

    def connect(self):
        """**************************************************
        Metodo que se encarga de conectar al contacto
        **************************************************"""
        try:
            if self.directory_ip != 'localhost':
                self.api_client.connect_contact(get_ip_address(),
                                                CHAT_PORT,
                                                self.username)
            else:
                self.api_client.connect_contact('localhost',
                                                self.my_port,
                                                self.username)
        except KeyError, e:
            print str(e)
            return False
        except Exception, e:
            print str(e)
            return False
        return True

    def disconnect(self):
        """**************************************************
        Metodo que se encarga de desconectar al contacto
        **************************************************"""
        self.api_client.disconnect_contact(self.username)
