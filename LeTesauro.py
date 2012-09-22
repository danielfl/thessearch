#!/usr/bin/env python
# -*- coding: utf-8 -*-

import Auxiliares as ax
import csv
import string

class LeTesauro:
	def __init__ (self, assunto='network'):
		self.aux = ax.Auxiliares()
                self.aux.printDebug("LeTesauro::")
		self.dt = csv.reader(file('thesaurus-'+assunto+'.txt'))
		self.registro=[]
		self.procurado=""

	def buscaTermo(self, termo, ptos=10): 
	        termos_pontos={}
		pontos=100 #pontos iniciais
		self.registro=[]
	        self.aux.printDebug("LeTesauro::buscaTermo(" +termo+ ")")
		self.procurado=termo
		for linha in self.dt:
			if linha[0] == termo: # termo origem encontrada e lista de sinonimos
				linha.remove("#")
				linha.remove("")
				
				for termo in linha:
					termos_pontos[termo]=pontos*int(ptos)
					
					if pontos > 10:
					      pontos -= 5 #reduz pontos por distancia do termo inicial
						
				return termos_pontos # retorna registro com todos os sinonimos encontrados

	def exibeTesauros(self):
		pontos=100 #pontuacao inicial
		for palavra in self.registro: 
			if palavra in ["#",""]: #procura linda
				continue
			self.aux.printDebug("Semelhante --> " , palavra, " ptos: ", pontos)
	#	if self.procurado == palavra: 
	#		print ": ! [" ,palavra , "]"
			#	print registro
			if pontos > 10:
				pontos-=5 #reduz pontos por distancia do termo inicial


