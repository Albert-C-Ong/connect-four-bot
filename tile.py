#!/usr/bin/python
# -*- coding: utf-8 -*- 

"""
Written by Albert Ong

Created: 2022.04.05
"""


class Tile:
	
	def __init__(self, color = None):
		
		self.color = color
	
	
	def __repr__(self):
		
		color = self.color
		
		if color == "red":
			return "X"
		elif color == "black":
			return "O"
		else:
			return "_"
	
		
	def filled(self):
		return self.color != None
