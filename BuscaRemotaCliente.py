# -*- coding: utf-8 -*-
#!/usr/bin/env python

import socket
import scriptutil as SU
import BuscaArquivo as ba
import pickle
from Auxiliares import Auxiliares

HOST = "127.0.0.1"
PORT = 42000

counter = 0

	
#TODO implementar segurança na procura, para nao deixar o daemon "inseguro" escutando numa porta
class BuscaRemotaCliente:
	def __init__(self):
		self.ips=[]
		print "Iniciando busca remota no servidor" 
		self.resultado=""
	        self.aux = Auxiliares()
		self.host=""
		self.port=42000
		self.termo=""

	def defineHost(self,host):
		self.host=host

	def definePort(self,port):
		self.port=port

	def obtemResultado(self):
		return self.resultado
		
	def busca(self, host, port, termo):
		sock=self.conectar(host, port) 
		if sock != -1:
			self.buscaRemota(sock, termo) 
			self.desconectar(sock) 

	def conectar(self, host, port): 
		mySocket = socket.socket( socket.AF_INET, socket.SOCK_STREAM ) 

		try:
			mySocket.connect( ( host, port ) )
			print "Connectado ao servidor"
		except:
			print "ERRO ao conectar"
			return -1
		
		return mySocket

	def desconectar(self, sock): 
		print "Conexao terminada!"
		sock.close()
	def defineListaMaquinas(self, lista_maquinas):
		self.lista_maquinas=lista_maquinas

	def obtemListaMaquinas(self):
		return self.lista_maquinas

	def buscaRemota(self, mySocket, termo):
		serverMessage = mySocket.recv( 1024 )
		if not serverMessage:
			return

		procura = ba.BuscaArquivo()
		procura.defineNomeArquivo(termo)
		if self.lista_maquinas:
			procura.defineListaMaquinas(self.obtemListaMaquinas())

		procura.defineDiretorio("/home/daniel/media/mp3")
		
		mySocket.send( pickle.dumps(procura) )
		self.aux.printDebug("Agente enviado")

		serverMessage = " " # mySocket.recv( 1024 )


		cli_resultado=""
		while serverMessage != "\n":
			serverMessage = mySocket.recv( 1024 ) 
			if serverMessage != "\n":
				cli_resultado+=serverMessage
#				print "recebendo["+serverMessage+"]"
			
		#	print clientMessage ,"", serverMessage 

		
		self.aux.printDebug("Agente recebido de volta")

		ag_procura=pickle.loads(cli_resultado)
		self.resultado=ag_procura.obtemResultado()


