#!/usr/bin/env python
# -*- coding: utf-8 -*-
#dead
import Auxiliares 
import csv
# A leitura recebe um objeto arquivo
dt = csv.reader(file('thesaurus-network.txt'))
# Para cada registro do arquivo, imprima
for reg in dt:
   print reg



