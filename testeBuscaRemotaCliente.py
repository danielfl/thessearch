#!/usr/bin/env python 

import BuscaRemotaCliente as brc
import scriptutil as SU

cli=brc.BuscaRemotaCliente()

#cli.conectar( "127.0.0.1" , 42000 )

cli.busca( "127.0.0.1" , 42000, "ola")
SU.printr(cli.obtemResultado())

