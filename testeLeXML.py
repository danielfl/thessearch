# -*- coding: utf-8 -*-
#!/usr/bin/env python

import LeXML as lx


# Esse arquivo vai conter todas as chamadas principais
lex = lx.LeXML()

for palavra in lex.getPalavrasCategoria("computacao grafica"):  
  print "Valor:", palavra.get('valor'), "pontos", palavra.get('pontos')

for palavras in lex.getPalavrasCategoria("network"):
  print "Valor:", palavras.get('valor'), "pontos", palavras.get('pontos')

print lex.obtemPercentualCategoria("network")