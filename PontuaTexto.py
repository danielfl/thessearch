#!/usr/bin/env python
# -*- coding: utf-8 -*-

import Auxiliares as ax
import Dicionario
import string
import re

#Pontuar de acordo com a relevancia do texto em relacao a palavra passada como parametro
class PontuaTexto:
        def __init__ (self, palavra, texto):
		self.aux     = ax.Auxiliares()
                self.aux.printDebug("PontuaTexto::")
                self.palavra = palavra
                self.pontos  = 0
                self.texto   = texto
                self.tags    = []
                self.setTagTexto(palavra) # "computacao grafica"

        def setTagTexto (self, palavra):
#                self.aux.printDebug("PontuaTexto::setTagTexto [" + palavra + "]")
                # se texto tiver relevancia suficiente com aquela palavra ele
                # recebe a tag que a palavra de entrada
                self.tags.append(palavra)

	def procuraPalavraTexto(self, termo, texto):
		# utilizar expressoes regulares
		self.aux.printDebug("PontuaTexto::procuraPalavraTexto")

		termo_atual=termo
		
		return string.count(texto, " "+termo_atual.lower()+" ")
			
		


#ptos = PontuaTexto.PontuaTexto("computacao grafica", "pixel e pixeis pixando por ai")
#palavra="computacao grafica"
#texto="pixel mouse monitor"

#dic = Dicionario.Dicionario(palavra, texto) 
#dic.procuraPalavraTexto( palavra, texto)

