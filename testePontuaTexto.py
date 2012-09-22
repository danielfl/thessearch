#!/usr/bin/env python
# -*- coding: utf-8 -*-

import PontuaTexto as pt



palavra="network" # categoria
texto="A lot of security network software made for internet location runs in a thin Linux box "

pote = pt.PontuaTexto(palavra, texto)
print pote.procuraPalavraTexto(palavra, texto)

