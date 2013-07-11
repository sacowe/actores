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
<<<<<<< HEAD
		query = "SELECT * FROM actor"
=======
		query = """SELECT * FROM actor"""
>>>>>>> database
		resultado = c.execute(query)
	except sqlite3.Error as e:
		exito = False
		print "Error:", e.args[0]
	prod = resultado.fetchall()
	con.close()
	return prod

<<<<<<< HEAD
if __name__ == "__main__":
	conectar()
=======
def get_peliculas_table():
	#devuelve la tabla peliculas completa
	con = conectar()
	c = con.cursor()
	try:
		query = """SELECT * FROM peliculas"""
		resultado = c.execute(query)
	except sqlite3.Error as e:
		exito = False
		print "Error:", e.args[0]
	prod = resultado.fetchall()
	con.close()
	return prod

def get_actor_has_peliculas():
	#devuelve la tabla actor_has_peliculas completa
	con = conectar()
	c = con.cursor()
	try:
		query = """SELECT * FROM actor_has_peliculas"""
		resultado = c.execute(query)
	except sqlite3.Error as e:
		exito = False
		print "Error:", e.args[0]
	prod = resultado.fetchall()
	con.close()
	return prod

def convert_to_array(data):
	lista = []
	for row in data:
		lista.append([row[0],row[1],row[2],row[3]])
	return lista

def dothis():
	print "g"

if __name__ == "__main__":
	dothis()
>>>>>>> database
