#!/usr/bin/env python 
# -*- coding: utf-8 -*-

import scriptutil as SU
import socket
import fcntl
from Auxiliares import Auxiliares
import struct 
from BaseBusca import BaseBusca

HOST = "127.0.0.1"
PORT = 42000 

class ProcuraMaquinas(BaseBusca):
	def __init__(self):
		print "Procura Maquinas"
	        self.aux = Auxiliares()
 		self.resultado=""
		self.lista_maquinas=[]

	def desconectar(self, sock): 
		print "Conexão terminada!"
		sock.close()

	def conectar(self, host, port): 
		mySocket = socket.socket( socket.AF_INET, socket.SOCK_STREAM ) 

		try:
			mySocket.connect( ( host, port ) )
			print "Connectado ao servidor"
		except:
			print "Nao foi possível conectar: ", host
			return -1
		
		return mySocket

	# montar um network scanner a partir da mascara de rede
	def scanMask(self, tripla, inicial, final):
		for ip1 in range(inicial, final):
			self.aux.printDebug("Numero IP: " , tripla+"."+str(ip1))
			self.scanHost(tripla+"."+str(ip1), PORT)
		return self.lista_maquinas

	def scanNet(self, hosts): 
		for host in hosts:
			self.scanHost(host, PORT)

		return self.lista_maquinas

	def scanHost(self, host, port): 
		res = self.conectar(host, port) 
		if res != -1:
			print "Maquina ", host, ":", PORT," pronta para a busca!"
			self.lista_maquinas.append(host)
			self.desconectar(res)
			return 1
		else:
			return -1


