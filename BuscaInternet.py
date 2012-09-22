# -*- coding: utf-8 -*-
#!/usr/bin/env python

import urllib, urllib2, time, socket, gzip, httplib, StringIO, re
from stripogram import html2text


class BuscaInternet:
	def __init__(self):
		self.opener = ""
	        self.conteudo=""
		
	def removerTagsHTML(self):
	    p = re.compile(r'<[^<]*?/?>')
	    return p.sub('', self.conteudo)

	def removerEspacos(self):
	    p = re.compile(r'\s+')
	    return p.sub(' ', self.conteudo)

	def obtemTexto(self):
	  self.conteudo=self.removerEspacos()
	  self.conteudo=self.removerTagsHTML()

	  return html2text(self.conteudo)


	def obtemHTML(self,url):# timeout in seconds
	  socket.setdefaulttimeout(5)

	  req = urllib2.Request(url)
	  response = urllib2.urlopen(req)
	  self.conteudo= response.read()

	  return self.conteudo

