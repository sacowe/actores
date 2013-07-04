#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3

def conectar():
	con = sqlite3.connect('main_database.db')
	con.row_factory = sqlite3.Row
	return con

def get_actor_table():
	#devuelve la tabla actor completa
	con = conectar()
	c = con.cursor()
	try:
		query = "SELECT * FROM actor"
		resultado = c.execute(query)
	except sqlite3.Error as e:
		exito = False
		print "Error:", e.args[0]
	prod = resultado.fetchall()
	con.close()
	return prod

if __name__ == "__main__":
	conectar()