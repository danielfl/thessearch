
# -*- coding: latin1 -*- 
import BuscaArquivo as ba
import socket 
import scriptutil as SU

procura = ba.BuscaArquivo()

procura.defineNomeArquivo("*mp3*")
procura.defineDiretorio("/home/daniel/media/mp3")

resultado=procura.buscaArquivo()

SU.printr(resultado)

#procura.buscaConteudo(".", "python")



