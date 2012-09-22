# -*- coding: utf-8 -*-
#!/usr/bin/env python

import scriptutil as SU

from LeXML import LeXML 	
from LeTesauro import LeTesauro  
from PontuaTexto import PontuaTexto 
from BuscaInternet import BuscaInternet 
from BuscaRemotaCliente import BuscaRemotaCliente
from ProcuraMaquinas import ProcuraMaquinas 
from BuscaArquivo import BuscaArquivo 
from Robo import Robo
from BaseBusca import BaseBusca
from Auxiliares import Auxiliares


class Procura(BaseBusca):
  def __init__(self, assunto="network"):
    self.lex = LeXML(assunto)
    self.termos_pontos={}
    self.aux = Auxiliares()
    self.pontuacao=0
    self.numero_palavras=0
    self.palavras_encontradas=0
    self.percentual_palavras_texto=0
    self.categoria_busca=""

  # Logica "Difusa" 
  #-----------------------
  # media >= 70%      - altamente relevante 
  # 30% < media < 70% - relevante 
  # media for <= 30%  - inrelevante 
  def fuzzinator(self):
    media=self.obtemPontosPorPalavra()/self.obtemPontosPorPalavraCategoria()
    
    if media >= 0.70:return "alta" 
    if media <= 0.30:return "baixa" 
    return "media"

  def obtemNumeroPalavrasEncontradas(self):
    return self.palavras_encontradas

  def obtemNumeroPalavras(self):
    return self.numero_palavras

  def obtemPontuacao(self): 
    #re read the XML file with the new information
    self.lex = LeXML()
    
    return self.pontuacao
    
  def obtemPontosPorPalavra(self):
    return float(self.obtemPontuacao())/float(self.obtemNumeroPalavras()) 

  def obtemPontosCategoria (self):
    return self.lex.obtemPontosCategoria()

  def obtemPalavrasCategoria (self):
    return self.lex.obtemPalavrasCategoria()
  
  def obtemPontosPorPalavraCategoria(self):
    return float(self.obtemPontosCategoria ())/float(self.obtemPalavrasCategoria ())
    
  def obtemPercentualPalavrasCategoria(self):
    return self.percentual_palavras_texto

  def obtemCategoria(self):
    return self.categoria_busca
    
  def procurarPontuar(self, categoria, texto=""):
    self.pontuacao=0
    ocorrencias=0
    if not texto: 
	texto=self.obtemConteudo()
    
    self.numero_palavras=len(texto.split(' '))
    self.percentual_palavras_texto=self.lex.obtemPercentualCategoria(categoria)
    self.categoria_busca=categoria
    
    
    # levantar pesos e pontos
    for palavras in self.lex.getPalavrasCategoria(categoria):
	let = LeTesauro()


	pot = PontuaTexto(palavras.get('valor').lower(), texto.lower())
	ocorrencias=pot.procuraPalavraTexto(palavras.get('valor').lower(), texto.lower())

	if ocorrencias != 0:
	  self.aux.printDebug("["+str(palavras.get('valor'))+ "]="+ str(palavras.get('pontos'))+ "*"+str(ocorrencias*110))
	  self.pontuacao += int(palavras.get('pontos'))*(ocorrencias*110) #se um sinonimo vale 100 a palavra q leva a ele tbm merece o merito
	  self.palavras_encontradas+=ocorrencias
	
	termos_pontos = let.buscaTermo(palavras.get('valor'), palavras.get('pontos'))

        #print termos_pontos
        # procurar para cada palavra
	if termos_pontos:
	   # self.aux.printDebug(termos_pontos)
	    for termo in termos_pontos:
	        self.aux.printDebug(termo)
		pote = PontuaTexto(termo.lower(), texto.lower())
		ocorrencias=pote.procuraPalavraTexto(termo.lower(), texto.lower())
		if ocorrencias != 0:
		  self.aux.printDebug("\t["+ termo+ "]="+str( termos_pontos[termo] )+ "*"+str( ocorrencias))
		  
		  self.pontuacao += termos_pontos[termo]*ocorrencias
		  self.palavras_encontradas+=ocorrencias
		  
  # defineConteudo:
  #  @meio: como os dados devem ser buscados
  #  @dados: e uma variavel que poder ter tipos diferentes de acordo com a necessidade, essa necessidade
  #         indica: meios para se obter a informacao a ser procurada
  def defineConteudo(self, meio, dados):
    
      print "-"*30

      if meio == 1:#"buscaremota":
	print "buscaremota"

	cli=BuscaRemotaCliente()

	ip=raw_input("Digite o ip: ")
	termo_procura=raw_input("Buscar: ") 
	
	cli.defineHost(ip) 
	cli.busca( ip , 42000, termo_procura)
	SU.printr(cli.obtemResultado())

      elif meio == 2:# "rede":
	print "rede" 

	tripla = raw_input("Digite a tripla: ") 
	inicio = raw_input("Digite o num inicial: ")
        final  = raw_input("Digite o num final: ") 
	termo_procura= raw_input("Digite o conteudo a procurar nos computadores encontrados: ") 

	if not tripla: tripla="127.0.0"
	if not inicio: inicio=1
	if not final: final=255


	cli=BuscaRemotaCliente() 

	a=1
	pm = ProcuraMaquinas() 
	for maquina in pm.scanMask(tripla, int(inicio), int(final)):
		a=0
		cli.busca( maquina , 42000, termo_procura)
		SU.printr(cli.obtemResultado())
	
	if a==1: print "Sem maquinas para conectar"

	#lista_maquinas = pm.scanMask(tripla, int(inicio), int(final))
	#
	#maquina=lista_maquinas.pop(0)
	#cli.defineHost(maquina) 
	#cli.defineListaMaquinas(lista_maquinas)
	#cli.busca( maquina , 42000, termo_procura)
	#SU.printr(cli.obtemResultado())
	#aqui entraria um codigo para aguardar o agente retornar com os dados das buscas pela rede

      elif meio == 3:# "internet":
	print "internet" 

	meuRobo = Robo() 
        site = raw_input("Digite o endereco do site: ") 
	if site: meuRobo.defineSite(site) 

	self.defineConteudo(meuRobo.obtemConteudo())

      elif meio == 4:# "local": #arquivos locais
	print "local"
	
	procura = BuscaArquivo()

	procura.defineNomeArquivo("*mp3*")
	procura.defineDiretorio("/home/daniel/media/mp3")

	resultado=procura.buscaArquivo()

	SU.printr(resultado)

	#procura.buscaConteudo(".", "python")
      elif meio == 5:#"texto":
	print "texto" 
	
	pr = Procura()                                

	pr.procurarPontuar("network", dados.lower())

	print "Categoria: ", pr.obtemCategoria().upper()
	print "\tPontos: \t[" , pr.obtemPontuacao() , "]"
	print "\tRelevancia: \t[", pr.fuzzinator().upper() , "]"
	print "\tPontos por palavra: \t[" , int(pr.obtemPontosPorPalavra()), "]"


#print pr.obtemPalavrasCategoria()
#print pr.obtemNumeroPalavras()
##print pr.obtemPercentualPalavrasCategoria()
#
#print pr.obtemPercentualPalavrasCategoria(), "",pr.obtemPontosPorPalavra(), ""
#print pr.obtemPontosPorPalavraCategoria() , "", pr.obtemPontosCategoria()

      else: print "Opcao Invalida"

      print "Fim."



