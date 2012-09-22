#!/usr/bin/env python
# -*- coding: utf-8 -*-

import scriptutil as SU
import re

class BuscaArquivo:
	def __init__ (self):
		print "BuscaArquivo->"
		self.nome_arquivo=""
		self.diretorio=""
		self.conteudo=""
		self.resultado=""
		self.lista_maquinas=[]

	def defineListaMaquinas(self, lista_maquinas):
		self.lista_maquinas=lista_maquinas

	def obtemListaMaquinas(self):
		return self.lista_maquinas

	def defineNomeArquivo(self, nomeArquivo):
		self.nome_arquivo=nomeArquivo 

	def defineConteudo(self, conteudo):
		self.conteudo=conteudo 

	def defineDiretorio(self, diretorio):
		self.diretorio=diretorio

	def obtemResultado(self):
		return self.resultado

	def obtemProximaMaquina(self):
		if self.lista_maquinas: 
			return self.lista_maquinas.pop(0)
		return -1

	def executa(self):
		self.buscaArquivo()

	def buscaArquivo(self):
		nomeArquivo=self.nome_arquivo
		diretorio=self.diretorio
		print "buscaArquivo::[", nomeArquivo, "]"

#		flist = SU.ffind(diretorio, shellglobs=("*"+nomeArquivo+"*"))
#		SU.printr(flist) 
		flist = SU.ffind(diretorio, shellglobs=("\*"+nomeArquivo+"\*"))
		#SU.printr(flist) 
		flist = SU.ffind(diretorio, shellglobs=(nomeArquivo, diretorio))
#		SU.printr(flist) 
		self.resultado=flist
		return flist

	#busca arquivo por conteudo

	def buscaConteudo(self): 
		conteudo=self.conteudo
		print "buscaConteudo::", conteudo

		flist = SU.ffindgrep(diretorio, regexl=(conteudo,))

		self.resultado=flist
		return flist
		#SU.printr(flist)

