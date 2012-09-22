# -*- coding: latin1 -*- 
#!/usr/bin/env python 

import BuscaArquivo as ba
import socket
import pickle

HOST = "127.0.0.1"
PORT = 42000 

class BuscaRemotaServidor: 
	def __init__(self):
		self.resultado = 0 
		counter = 0 
		mySocket = socket.socket( socket.AF_INET, socket.SOCK_STREAM )

		mySocket.bind( ( HOST, PORT ) )
		while 1: 
			print "Aguardando conexoes"
			mySocket.listen( 1 )

			connection, address = mySocket.accept()
			counter += 1
			print "Conexão ", counter, "de: ", address[ 0 ]

			connection.send( "Servidor: Ouvindo" )
			try:
				clientMessage = connection.recv( 1024 )
			except:
				print "Não consegui receber dados"
				continue

			ag_procura=pickle.loads(clientMessage)
			ag_procura.executar() 
			#aqui o agente procuraria a proxima maquina para se conectar 


			# usar rotinas do gzip para compactar informação antes de enviar
			connection.send( pickle.dumps(ag_procura) )
			connection.send( "\n" )

			print "Agente enviado de volta" 

			clientMessage = connection.recv( 1024 )

			connection.close()

			print "Conexão terminada" 

	def busca(self, palavra): 
		print "Buscando: ", palavra
		procura = ba.BuscaArquivo()
		#ba.buscaArquivo(".","busca")
		self.resultado=procura.buscaArquivo(".", palavra)
		#resultado=procura.buscaConteudo(".", palavra)
		#resultado=procura.buscaConteudo(".","python")


