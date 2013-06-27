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
	populate_actor_has_peliculas(con)
	con.commit()

def conect():
	con = sqlite3.connect('main_database.db')
	con.text_factory = str
	return con

def create_actor(con):
	c = con.cursor()
	query = """CREATE TABLE actor(id_actor integer PRIMARY KEY AUTOINCREMENT,
									nombre text, 
									birthday date, 
									genero text, 
									imagen text)"""
	c.execute(query)

def populate_actor(con):
	c = con.cursor()
	query = """INSERT INTO actor(nombre,birthday,genero,imagen) VALUES (?,?,?,?)"""
	for i in info.actores:
		c.execute(query,i)

def create_peliculas(con):
	c = con.cursor()
	query = """CREATE TABLE peliculas(id_pelicula integer PRIMARY KEY AUTOINCREMENT,
										nombre text, 
										estreno date, 
										director text, 
										descripcion text)"""
	c.execute(query)

def populate_peliculas(con):
	c = con.cursor()
	query = """INSERT INTO peliculas(nombre,estreno,pais,descripcion) VALUES (?,?,?,?)"""
	for i in info.peliculas:
		c.execute(query,i)

def create_actor_has_peliculas(con):
	c = con.cursor()
	query = """CREATE TABLE actor_has_peliculas(fk_id_actor int,
												fk_id_pelicula int,
												personaje text,
												descripcion_rol text,
												FOREIGN KEY(fk_id_pelicula) REFERENCES peliculas(id_pelicula),
												FOREIGN KEY(fk_id_actor) REFERENCES actor(id_actor))"""
	c.execute(query)

def populate_actor_has_peliculas(con):
	c = con.cursor()
	query = """INSERT INTO actor_has_peliculas VALUES (?,?,?,?)"""
	for i in info.relaciones:
		c.execute(query,i)

if __name__ == '__main__':
	main()