#!/usr/bin/env python
# -*- coding: utf-8 -*-

import httplib, sys, re
from HTMLParser import HTMLParser
from stripogram import html2text
from BaseBusca import BaseBusca

class Robo( HTMLParser, BaseBusca ):
  linksVisitados = []
  filaLinks = []
  site="localhost"
  link="/"
  cache=""

  #nao suporta criptografia de dados

  def defineSite(self, site):
    self.site=site

  def defineLink(self, link):
    self.link=link

  def proximoLink( self ):
    if self.filaLinks == []:
      return ''
    else:
      self.link=self.filaLinks.pop(0)
      return self.link


  def obtemHTML(self):
    try:
      httpconn = httplib.HTTPConnection(self.site)
      httpconn.request("GET", self.link)
      resp = httpconn.getresponse()
      html = resp.read()
      
      self.cache=self.cache+html2text(html)
    except:
      html = ""

    self.feed(html)
    if self.proximoLink() != '':
      self.obtemHTML()

      return html

  def removerEspacos(self):
      p = re.compile(r'\s+')
      self.cache = p.sub(' ', self.cache)

  def handle_starttag( self, tag, attrs ):
    if tag == 'a':
      newstr = str(attrs[0][1])
      if re.search('http|mailto', newstr) == None and re.search('htm|php', newstr) != None and (newstr in self.linksVisitados) == False:
         self.filaLinks.append( newstr )
         self.linksVisitados.append( newstr )
  def obtemResultado(self):
	return self.obtemConteudo()
    
  def obtemConteudo(self):
    self.obtemHTML()
    self.removerEspacos()
    self.defineResultado(self.cache)

    print "Conteudo: " + self.cache

    return self.cache


