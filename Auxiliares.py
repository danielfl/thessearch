#!/usr/bin/env python
import config


class Auxiliares: 
	def __init__ (self):
		self.debug=config.debug 

	def printDebug(self, texto):
		if self.debug==True:
			print "DEBUG: "+texto




