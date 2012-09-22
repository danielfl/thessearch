#!/usr/bin/env python
# -*- coding: utf-8 -*-

from stripogram import html2text
import BuscaInternet as bin

url = 'http://danielfl.wordpress.com/2008/10/12/fisl9-slack-configuration-management-system-for-lazy-sysadmins/' 

# Busca Internet
bi = bin.BuscaInternet()
bi.obtemHTML(url)

#print str(texto)
print url
#bi.removerEspacos()
print bi.obtemTexto()
