#!/usr/bin/env python
# -*- coding: utf-8 -*-


class BaseBusca:
  resultado=""
  def __init__(self):
      self.resultado=""

  def obtemResultado(self):
    return self.resultado

  def defineResultado(self, resultado):
    self.resultado=resultado

  def executa(self):
    print

