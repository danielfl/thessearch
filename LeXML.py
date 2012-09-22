# -*- coding: utf-8 -*-
#!/usr/bin/env python

from xml.etree.ElementTree import ElementTree

class LeXML:
	def __init__ (self, assunto='network'):
		tree = ElementTree(file=assunto+'.xml')
		self.root = tree.getroot()
		self.valPto=[]


	def obtemPercentualCategoria (self, palavra):
		self.valPto=[]

		lobo = self.root.find('categoria')
		return lobo.get('percentual')
	      
	def obtemPontosCategoria (self):
		self.valPto=[]

		lobo = self.root.find('categoria')
		return lobo.get('pontos')

	def obtemPalavrasCategoria (self):
		self.valPto=[]

		lobo = self.root.find('categoria')
		return lobo.get('palavras')
		


	def getPalavrasCategoria (self, palavra):
		self.valPto=[]
		#print palavra

		lobo = self.root.find('categoria')
		
		if lobo.get('nome') == palavra:
			#print lobo.get('nome'), " : " , palavra	
			if lobo != None : 
				for node in lobo: 
					self.valPto.append(node)
					#print ".. " , node.get('valor') , " " , node.get('pontos')	
	        else:
		#	print lobo.get('nome'), " : " , palavra	
			if lobo != None : 
				for node in lobo: 
					self.valPto.append(node)
					#print ".. " , node.get('valor') , " " , node.get('pontos')	
		#	print lobo.get('nome')

		return self.valPto
	
	def listaCategorias(self):
	  lobo = self.root.find('categoria')
	  #print lobo.get('nome')
	  for lobo in self.root.find('categoria'):
	    
	    if lobo != None : 	
		      print lobo.get('nome'), " : "

		      for node in lobo: 
			    print ".. " , node.get('valor') , " " , node.get('pontos')	
			  
	  for lobo in self.root.find('categoria'):
	    if lobo != None: 				
	      for node in lobo: 
		print "Nome:" +node

