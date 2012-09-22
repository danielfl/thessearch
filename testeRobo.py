#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from Robo import Robo

meuRobo = Robo()

meuRobo.defineSite("www.kernel.org")
meuRobo.defineLink("/pub/linux/kernel/v2.6/")


print meuRobo.obtemResultado()

