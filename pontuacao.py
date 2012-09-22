#!/usr/bin/env python
# -*- coding: utf-8 -*-

#import pontuatexto
#import pontuacao
import Dicionario


palavra="computacao grafica" # categoria
texto="Os monitor eh cheio de pixels, mesa-digitalizadora quem mexe o cursor na tela eh o mouse "

dic = Dicionario.Dicionario(palavra, texto) 
dic.procuraPalavraTexto(palavra, texto)


