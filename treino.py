# -*- coding: utf-8 -*-
import string

#numero de palavras de rede encontradas em um texto conhecido sobre redes
#numero de palavras encontradas em um texto conhecido sobre redes 
#media de palavras de rede de um texto sobre rede

#numero de palavras de rede encontradas no texto qualquer
#numero de palavras encontradas no texto qualquer
#media de palavras de redes do texto qualquer

palavras_rede="network communication alive packet router switches ethernet wireless internet telecom"

#########

palavras="working network is when ethernet wireless internet telecom the state of the communication is keeping alive with the packet descriptions with route switches and anything else" 

num_palavras_texto_conhecido = len(palavras.split(' ')) 
num_palavras_de_rede_texto_conhecido = 0 
for word in palavras.split(' '):
	if string.find(palavras_rede, word) != -1:
		num_palavras_de_rede_texto_conhecido+=1
		
media_termos_rede_texto_conhecido=(float(num_palavras_de_rede_texto_conhecido) / float(num_palavras_texto_conhecido)) 
print "num_palavras_texto_conhecido ", num_palavras_texto_conhecido
print "num_palavras_de_rede_texto_conhecido=",num_palavras_de_rede_texto_conhecido 
print "media de palavras: %-14f"  %  media_termos_rede_texto_conhecido 
print ""

###########

texto_qualquer="the computer network maybe a good thing"

num_palavras_texto_qualquer=len(texto_qualquer.split(' '))
num_palavras_de_rede_texto_qualquer= 0 
for palavra in texto_qualquer.split(' '):
	if string.find(palavras_rede, palavra) != -1:
		num_palavras_de_rede_texto_qualquer+=1

media_termos_rede_texto_qualquer=(float(num_palavras_de_rede_texto_qualquer) / float(num_palavras_texto_qualquer))

print "num_palavras_texto_qualquer", num_palavras_texto_qualquer
print "num_palavras_de_rede_texto_qualquer=", num_palavras_de_rede_texto_qualquer 
print "media de palavras: %-14f" % media_termos_rede_texto_qualquer
print ""


media_termos=(media_termos_rede_texto_qualquer / media_termos_rede_texto_conhecido)
###############################

# Logica Difusa Caseira
#-----------------------
# media >= 70%      - altamente relevante 
# 30% < media < 70% - relevante 
# media for <= 30%  - inrelevante 

def fuzzinator(media):
	if media >= 0.70:return "alta" 
	if media <= 0.30:return "baixa" 

	return "media"


print "Relevancia do texto qualquer:", fuzzinator(media_termos)


