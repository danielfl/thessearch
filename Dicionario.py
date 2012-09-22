#!/usr/bin/env python 
# -*- coding: utf-8 -*-
#dead!
import LeXML
import Auxiliares
import re
import string

# Contem a relacao de dicionarios
class Dicionario:
	def __init__ (self, palavra, texto):
		self.aux = auxiliares.Auxiliares()
		self.total_pontos=0
		self.aux.printDebug("Dicionario::")
		self.dicionario= {   # dicionario > palavra > pontuacao 
				'computacao grafica'  : {
					     'pixel'  : 10,
					     'pixels' : 10,
					     'mouse'  : 10,
					     'mouses' : 10,
					     'monitor':  2,
					     'monitors' :2,
					     'monitores':2,
					     'mesa-digitalizadora': 3
				     }
		     }

		self.lista_palavras={
				'computacao grafica'  : {
					'0':'pixels',
					'1':'pixel',
					'2':'mouses',
					'3':'mouse',
					'4':'monitores',
					'5':'monitors',
					'6':'monitor',
					'7':'mesa-digitalizadora'
			}
		}

		self.palavra = palavra
		self.texto   = texto 

	def findall(self, L, value, start=0):
		# generator version
		i = start - 1
		try:
		    i = L.index(value, i+i)
		    yield i
		except ValueError:
		    pass
	
		
	def procuraPalavraTexto(self, palavra, texto):
		# utilizar expressoes regulares
		self.aux.printDebug("Dicionario::procuraPalavraTexto")

		space = re.compile(r'\s+') # quebra em palavras
		palavras_texto = space.split(texto) 

		# pontos para a palavra pixel no dicionario computacao grafica
		for iword in range(len(self.dicionario[palavra])):
			npal=str(iword)

			palavra_atual = self.lista_palavras[palavra][npal] 

			if string.find(texto , palavra_atual) != -1: 
				self.aux.printDebug("Dicionario::procuraPalavraTexto [" + palavra_atual + "]")
				self.total_pontos += self.dicionario[palavra][self.lista_palavras[palavra][npal]] 
				self.aux.printDebug("Pontos: " + str(self.dicionario[palavra][self.lista_palavras[palavra][npal]])) 
				self.aux.printDebug("Pontos acumulados: "+str(self.dicionario[palavra][self.lista_palavras[palavra][npal]])) 

		print "Total de pontos: "+str(self.total_pontos)+" categoria: " + palavra 
		print "Texto: "+texto 
				
		return 0 
	
