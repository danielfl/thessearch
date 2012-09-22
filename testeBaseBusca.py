#!/usr/bin/env python
# -*- coding: utf-8 -*-
from BaseBusca import BaseBusca
class teste(BaseBusca):

  
  def ola(self):
    print "ola"


t=teste()

t.defineResultado("oooooooooo")
print t.obtemResultado()
  
