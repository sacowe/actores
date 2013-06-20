#!/usr/bin/python
# -*- coding: utf-8 -*-
#Creando base de datos

import sqlite3
import info

def main():
	con = conect()
	create_actor(con)
	populate_actor(con)
	create_peliculas(con)
	populate_peliculas(con)
	create_actor_has_peliculas(con)

def conect():
	con = sqlite3.connect('main_database.db')
	return con

def create_actor(con):
	c = con.cursor()
	query = """CREATE TABLE actor(id_actor PRIMARY KEY int, 
									nombre text, 
									birthday date, 
									genero text, 
									imagen text)"""
	c.execute(query)

def populate_actor(con):
	#Llenar tabla actor

def create_peliculas(con):
	c = con.cursor()
	query = """CREATE TABLE peliculas(id_pelicula PRIMARY KEY int,
										nombre text, 
										estreno date, 
										pais text, 
										descripcion text""")
	c.execute(query)

def populate_peliculas(con):
	#Llenar tabla peliculas

def create_actor_has_peliculas(con):
	#crear tabla actor_has_peliculas


if __name__ == '__main__':
	main()