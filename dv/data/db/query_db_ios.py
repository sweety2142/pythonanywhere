from __future__ import with_statement
import sqlite3
from flask import _app_ctx_stack
from pprint import pprint as pp

def connect_db(db):
	return sqlite3.connect(db)
	
def init_db(db, sql):
	with closing(connect_db(db)) as db:
		with app.open_resource(sql) as f:
			db.cursor().executescript(f.read())
		db.commit()
		
def get_db(db):
	top = _app_ctx_stack.top
	if db:
		top.sqlite_db = sqlite3.connect(db)
	return top.sqlite_db
	
def update_db(db, query, request_form=()):
	db = get_db(db)
	db.execute(query, request_form)
	db.commit()
	
def query_db(db, query, args=(), oneline=False, line_num=0):
	cur = get_db(db).execute(query, args)
	rv = cur.fetchall()
	cur.close()
	return (rv[line_num] if rv else None) if oneline else rv
	
def select_query(table_name, selection='*'):
	return 'select ' + selection + ' from ' + table_name
	
def update_query(table_name, set_vars, where_var):
	query = 'update ' + table_name + ' set '
	for i in range(len(set_vars)):
		query += (set_vars[i] + ' = ?')
		if i == len(set_vars) - 1:
			query += ' where '
		else:
			query += ', '
			
	query += where_var + ' = ?'
	return query
	
def insert_query(table_name, insert_vars, n):
	return 'insert into '+ table_name + ' ' + insert_vars + ' values ( ' + '?, '*(n-1) + '?)'
	
def delete_query(table_name, where_var):
	return 'delete from ' + table_name + ' where ' + where_var + ' =?'
	
#####
def get_name(path):
  conn = sqlite3.connect('buyer.db')
  cur = conn.cursor()
  po = cur.execute("select name from sqlite_master WHERE type='table';")
  po = cur.fetchall()
  colname = cur.execute("select sql from sqlite_master where name='"+po[0][0]+"'")
  colname = cur.fetchall()
  print('table_name: ',po[0][0])
  #print('column_name: ',colname)
  pp(colname)
  print("--"*10)
  p = cur.execute("select * from BUYER").fetchall()
  pp(p)
  
  conn.close()

get_name('user_list.db')
