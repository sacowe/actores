#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3
from array import *

def conectar():
	con = sqlite3.connect('main_database.db')
	con.row_factory = sqlite3.Row
	return con

def get_actor_table():
	#devuelve la tabla actor completa
	con = conectar()
	c = con.cursor()
	try:
		query = """SELECT * FROM actor"""
		resultado = c.execute(query)
	except sqlite3.Error as e:
		exito = False
		print "Error:", e.args[0]
	prod = resultado.fetchall()
	con.close()
	return prod

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
	
def get_peliculas_by_name(arg):
	#devuelve la tabla peliculas completa
	con = conectar()
	c = con.cursor()
	try:
		query = """SELECT * FROM peliculas WHERE nombre LIKE ?"""
		resultado = c.execute(query,["%"+arg+"%"])
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

def actors_from_movie(name):
	#devuelve las peliculas del actor "name".
	i = 0
	prod = []
	con = conectar()
	c = con.cursor()
	query1 = "SELECT id_pelicula FROM peliculas WHERE nombre = ?"
	query2 = "SELECT fk_id_actor FROM actor_has_peliculas WHERE fk_id_pelicula = ?"
	query3 = "SELECT * FROM actor WHERE id_actor = ?"
	try:
		res = c.execute(query1,[name])
		res = res.fetchone()
		res = c.execute(query2,[res[0]])
		res = res.fetchall()
		for r in res:
			answer = c.execute(query3,[r[0]])
#			prod.resize(i+1)
			prod.append(answer.fetchone())
			i = i + 1
	except sqlite3.Error as e:
		exito = False
		print "Error:", e.args[0]
	con.close()
	return prod

def convert_to_array(data):
	lista = []
	for row in data:
		lista.append([row[0],row[1],row[2],row[3]])
	return lista

def search_data_pel(name):
	con = conectar()
	c = con.cursor()
	try:
		query = """SELECT * FROM peliculas WHERE nombre=?"""
		resultado = c.execute(query,[name])
	except sqlite3.Error as e:
		exito = False
		print "Error:", e.args[0]
	prod = resultado.fetchall()
	con.close()
	return prod

def search_data_act(name):
	con = conectar()
	c = con.cursor()
	try:
		query = """SELECT * FROM actor WHERE nombre=?"""
		resultado = c.execute(query,[name])
	except sqlite3.Error as e:
		exito = False
		print "Error:", e.args[0]
	prod = resultado.fetchall()
	con.close()
	return prod

if __name__ == "__main__":
	dothis()
