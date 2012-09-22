# -*- coding: utf-8 -*-
#!/usr/bin/env python

from procura import Procura
from LeXML  import LeXML 




texto="""For semantic indexing we proposed the semantic pathﬁnder,for details see [4]. 
First, it extracts features from the visual [5],textual, and auditory modality. 
The architecture exploits super-vised machine learning to automatically label 
segments with semantic concepts. In the ﬁrst step learning is on the 
contentfeatures only. In the second step, the video is analyzed based on its 
style properties. Finally, semantic concepts are analyzed in context, with the 
potential to boost index results further. The resulting thesaurus of 500 semantic 
concepts, covering setting, objects, and people, is learned based on the 
LSCOM annotations [6] and the 101 concepts used in our 2005 engine [2].
"""

texto9="""The Internet is now a household term in many countries. With otherwise serious people 
beginning to joyride along the Information Superhighway, computer networking seems to be moving 
toward the status of TV sets and microwave ovens. The Internet has unusually high media coverage
, and social science majors are descending on Usenet newsgroups, online virtual reality environments, 
and the Web to conduct research on the new "Internet Culture."
Of course, networking has been around for a long time. Connecting computers to form local area 
networks has been common practice, even at small installations, and so have long-haul links using 
transmission lines provided by telecommunications companies. A rapidly growing conglomerate of 
world-wide networks has, however, made joining the global village a perfectly reasonable option 
for even small non-profit organizations of private computer users. Setting up an Internet host with
 mail and news capabilities offering dialup and ISDN access has become affordable, and the advent of
 DSL (Digital Subscriber Line) and Cable Modem technologies will doubtlessly continue this trend.
"""

# Esse arquivo vai conter todas as chamadas principais
pr = Procura()

print """
Entre com a opcao desejada:
  1. Buscaremota
  2. Rede
  3. Internet
  4. Local
  5. Texto
"""
op=raw_input("Escolha: ")

#pr.defineConteudo(int(op), texto)

pr.procurarPontuar("network", texto.lower())

print "Categoria: ", pr.obtemCategoria().upper()
print "\tPontos: \t[" , pr.obtemPontuacao() , "]"
print "\tRelevancia: \t[", pr.fuzzinator().upper() , "]"
print "\tPontos por palavra: \t[" , int(pr.obtemPontosPorPalavra()), "]"
