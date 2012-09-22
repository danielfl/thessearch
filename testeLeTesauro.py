#!/usr/bin/env python
# -*- coding: utf-8 -*-

import LeTesauro as lt

let = lt.LeTesauro()

linha=let.buscaTermo("close",10)
print linha
#let.exibeTesauros()

linha=let.buscaTermo("thin",10)
print linha
