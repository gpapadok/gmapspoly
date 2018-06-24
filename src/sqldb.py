#!/usr/bin/python3
import MySQLdb
from data import *

def dbinit():
	names = ["Solutions Informatics", "Plateia Georgiou", \
				"Lidl Akti Dimeon", "HMTY UPatras"]
	kml_names = ["solutions", "pl.georgiou", "lidl", "hmty"]

	db = MySQLdb.connect(host, user, pwd)
	cursor = db.cursor()

	try:
		cur.execute("CREATE DATABASE SOLMAPS")
		print("database SOLMAPS created")
	except:
		print("database SOLMAPS already exists")
	

	cur.execute("USE SOLMAPS")

	cur.execute("DROP TABLE IF EXISTS PLACES;")
	sql = """CREATE TABLE PLACES (
			name CHAR(255) NOT NULL,
			address CHAR(255),
			phone CHAR(16),
			zip CHAR(8),
			kml_name CHAR(255) )"""
	cur.execute(sql)

	for j in range(len(names)):
		sql = """INSERT INTO PLACES(name, kml_name) 
				 VALUES ("{}", "{}");""".format(names[j], kml_names[j])
		
		try:
			cur.execute(sql)
			db.commit()
		except:
			db.rollback()

	cursor.close()
	db.close()


def getnamelist():
	db = MySQLdb.connect(host, user, pwd, database)
	cursor = db.cursor()

	sql = "SELECT * FROM PLACES;"
	cursor.execute(sql)
	results = cursor.fetchall()

	names = []
	for row in results:
		names.append(row[0])

	cursor.close()
	db.close()

	return names


def getpolyname(name):
	db = MySQLdb.connect(host, user, pwd, database)
	cursor = db.cursor()
	
	sql = """SELECT * FROM PLACES WHERE name = "{}";""".format(name)
	cursor.execute(sql)
	result = cursor.fetchone()
	kml_name = result[4]

	cursor.close()
	db.close()

	return kml_name



if __name__ == '__main__':
	dbinit()





