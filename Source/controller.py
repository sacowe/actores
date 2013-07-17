#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3
from array import *

def conectar():
	#conecta base de datos
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

def delete_peliculas(arg):
	#elimina un elemento de la tabla peliculas
	con = conectar()
	c = con.cursor()
	try:
		query = """DELETE FROM peliculas WHERE nombre = ?"""
		resultado = c.execute(query,[arg])
	except sqlite3.Error as e:
		exito = False
		print "Error:", e.args[0]
	con.commit()
	con.close()
	return True

def delete_actor(arg):
	#Elimina una fila de la tabla actor.
	con = conectar()
	c = con.cursor()
	try:
		query = """DELETE FROM actor WHERE nombre = ?"""
		resultado = c.execute(query,[arg])
	except sqlite3.Error as e:
		exito = False
		print "Error:", e.args[0]
	con.commit()
	con.close()
	return True

def search_peliculas_name(arg):
	#devuelve la tabla peliculas completa con el nombre arg.
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
	
def search_peliculas_direc(arg):
	#devuelve la tabla peliculas completa con el nombre del director arg.
	con = conectar()
	c = con.cursor()
	try:
		query = """SELECT * FROM peliculas WHERE pais LIKE ?"""
		resultado = c.execute(query,["%"+arg+"%"])
	except sqlite3.Error as e:
		exito = False
		print "Error:", e.args[0]
	prod = resultado.fetchall()
	con.close()
	return prod
	
def search_peliculas_year(arg):
	#devuelve la tabla peliculas completa del año arg.
	con = conectar()
	c = con.cursor()
	try:
		query = """SELECT * FROM peliculas WHERE estreno LIKE ?"""
		resultado = c.execute(query,[arg+"%"])
	except sqlite3.Error as e:
		exito = False
		print "Error:", e.args[0]
	prod = resultado.fetchall()
	con.close()
	return prod
	
def search_actor_name(arg):
	#devuelve la tabla actores completa con el nombre arg.
	con = conectar()
	c = con.cursor()
	try:
		query = """SELECT * FROM actor WHERE nombre LIKE ?"""
		resultado = c.execute(query,["%"+arg+"%"])
	except sqlite3.Error as e:
		exito = False
		print "Error:", e.args[0]
	prod = resultado.fetchall()
	con.close()
	return prod
	
def search_actor_sex(arg):
	#devuelve la tabla actores completa con los actores de algun sexo.
	con = conectar()
	c = con.cursor()
	try:
		query = """SELECT * FROM actor WHERE genero LIKE ?"""
		resultado = c.execute(query,[arg+"%"])
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
	#Devuelve los actores de la pelicula "name".
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
			prod.append(answer.fetchone())
			i = i + 1
	except sqlite3.Error as e:
		exito = False
		print "Error:", e.args[0]
	con.close()
	return prod

def add_pelicula(name,director,fecha,desc):
	#Agrega una fila en la tabla pelicula con los valores entregados.
	con = conectar()
	c = con.cursor()
	try:
		query = """INSERT INTO peliculas(nombre,estreno,pais,descripcion) VALUES (?,?,?,?)"""
		resultado = c.execute(query,[name,fecha,director,desc])
		query = """SELECT id_pelicula FROM peliculas WHERE nombre = ?"""
		resultado = c.execute(query,[name])
	except sqlite3.Error as e:
		exito = False
		print "Error:", e.args[0]
	index = c.fetchone()
	con.commit()
	con.close()
	return index

def edit_pelicula(index,name,director,fecha,desc):
	#Edita una fila en la tabla pelicula con los valores entregados.
	con = conectar()
	c = con.cursor()
	try:
		query = """UPDATE peliculas SET nombre = ? ,estreno = ?,pais = ?, descripcion = ? WHERE id_pelicula = ?"""
		resultado = c.execute(query,[name,fecha,director,desc,index])
	except sqlite3.Error as e:
		exito = False
		print "Error:", e.args[0]
	index = c.fetchone()
	con.commit()
	con.close()
	return True

def add_actor(name,birth,gen):
	#Agrega una fila a la tabla actor con los valores entregados.
	con = conectar()
	c = con.cursor()
	try:
		query = """INSERT INTO actor (nombre, birthday, genero) VALUES (?,?,?)"""
		resultado = c.execute(query,[name,birth,gen])
	except sqlite3.Error as e:
		exito = False
		print "Error:", e.args[0]
	index = c.fetchone()
	con.commit()
	con.close()
	return True
	
def edit_actor(name,birth,gen,num):
	#Edita una fila en la tabla actor con los valores entregados.
	con = conectar()
	c = con.cursor()
	try:
		query = """UPDATE actor SET nombre = ?, birthday = ?, genero = ? WHERE id_actor = ?"""
		resultado = c.execute(query,[name,birth,gen,num])
	except sqlite3.Error as e:
		exito = False
		print "Error:", e.args[0]
	index = c.fetchone()
	con.commit()
	con.close()
	return True

def add_relation(pelicula,actor):
	#Agrega Foreing Keys en la tabla que relaciona actores con una pelicula.
	con = conectar()
	c = con.cursor()
	try:
		for i in actor:
			query = """SELECT * FROM actor WHERE nombre=?"""
			resultado = c.execute(query,[i])
			resultado = resultado.fetchone()
			query = """INSERT INTO actor_has_peliculas(fk_id_actor,fk_id_pelicula) VALUES (?,?)"""
			resultado = c.execute(query,[resultado[0],pelicula])
	except sqlite3.Error as e:
		exito = False
		print "Error:", e.args[0]
	con.commit()
	con.close()
	
def clear_relation(pelicula):
	#Agrega Foreing Keys en la tabla que relaciona actores con una pelicula.
	con = conectar()
	c = con.cursor()
	try:
		query = """DELETE FROM actor_has_peliculas WHERE fk_id_pelicula = ?"""
		resultado = c.execute(query,[pelicula])
	except sqlite3.Error as e:
		exito = False
		print "Error:", e.args[0]
	con.commit()
	con.close()
	return True

def search_data_act(name):
	#Obtiene la fila de nombre "name" en la tabla actores.
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

def search_data_pel(name):
	#Obtiene la fila de nombre "name" en la tabla peliculas.
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
	
def request_act(num):
	#Retorna verdadero si una id_actor ya se encuentra en la DB.
	con = conectar()
	c = con.cursor()
	try:
		query = """SELECT * FROM actor WHERE id_actor=?"""
		resultado = c.execute(query,[num])
	except sqlite3.Error as e:
		exito = False
		print "Error:",e.args[0]
	prod = resultado.fetchone()
	con.close()
	if prod is not None:
		return True
	else:
		return False
