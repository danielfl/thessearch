#! /usr/bin/python
# -*- coding: utf-8 -*-

import string
from string import punctuation
from operator import itemgetter 
import procura


#criar rotina de retreino
class Ensinar:
  def __init__ (self, arq, categoria):

    self.categoria = categoria
    self.xml=""
    self.max_palavras = 25 #MAX palavras XML
    self.arquivo = arq

    # palavras 'inuteis'
    palavras="""the to a is of and in it for that are be this with as do on can not an 
by at if all have from has one will or each which when but we its data some other 
so was used more up may many time there after before alice bob end much like 
using than been over same just different who whose number 0 1 2 3 4 5 6 7 8 9  their 
first second into how them does way new what who only now any called about 
they also these then use two example kind mean both between 
"""
    
    N = 200
    words = {}
    words_gen = (word.strip(punctuation).lower() for line in open(self.arquivo)
					         for word in line.split())

    num_palavras_texto_categorizado=0
    for word in words_gen:
      words[word] = words.get(word, 0) + 1
      num_palavras_texto_categorizado+=1

    #num_palavras_texto_categorizado=str(len(words.items()))

    top_words = sorted(words.iteritems(), key=itemgetter(1), reverse=True)[:N]
    
    i=tot=0
    for w,f in top_words:
      if string.find(palavras, w) != -1: continue
      if i>self.max_palavras: break
      tot=tot+f
    
    

    perc_palavras_categoria=(float(tot) / float(num_palavras_texto_categorizado)) 
    print "Palavras categoria:", tot, "de", num_palavras_texto_categorizado, "=", perc_palavras_categoria
    self.xml="<dicionarios>\n\
	<categoria nome='"+categoria+"' pontos='PONTOS' palavras='"+str(num_palavras_texto_categorizado)+"' percentual='"+str(perc_palavras_categoria)+"'>"
    n=1
    for word, frequency in top_words:
      if string.find(palavras, word) != -1: continue
      if n>self.max_palavras: break
      palavras=palavras+" "+word+"s"
    
      self.xml=self.xml+"\n\t\t<palavra indice='%d' valor='%s' pontos='%d' />" % (n, word, (float(frequency)/float(tot))*1000) 
      n+=1

    self.xml=self.xml+"""\n	</categoria>
</dicionarios>\n"""
    #print palavras

  def gravaXML(self):
    arq = file("dict-"+self.categoria+".xml", "w")
    arq.write(self.xml)
  
  def obtemXML(self):
    return self.xml

  def regravaXML(self, pontos):
    self.xml = self.xml.replace("PONTOS", str(pontos))
    self.gravaXML()


categoria="network" 
arquivo="tanenbaum.txt"

ens = Ensinar(arquivo, categoria)

ens.gravaXML()

#disparar o treino contra ele mesmo afim de obter a pontuacao do texto e usar como 
#base de um texto "que contem conteudo da categoria apresentada"

pr = procura.Procura()
pr.procurarPontuar(categoria, open(arquivo).read().lower())

ens.regravaXML(pr.obtemPontuacao())
#print ens.obtemXML()
print "Categoria: ", pr.obtemCategoria().upper()
print "\tPontos: \t[" , pr.obtemPontuacao() , "]"
print "\tRelevancia: \t[", pr.fuzzinator().upper() , "]"
print "\tPontos por palavra: \t[" , int(pr.obtemPontosPorPalavra()), "]"

#print pr.obtemPercentualPalavrasCategoria()
#print pr.obtemPontosPorPalavraCategoria()


