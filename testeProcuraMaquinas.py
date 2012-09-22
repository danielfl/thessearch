#!/usr/bin/env python 

# -*- coding: latin1 -*- 

import ProcuraMaquinas

pm = ProcuraMaquinas.ProcuraMaquinas()

pm.scanNet(["127.0.0.1","127.0.0.2", "127.0.0.3"])
pm.scanMask("127.0.0", 1, 25)

