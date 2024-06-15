from __future__ import with_statement
import sqlite3
from flask import _app_ctx_stack

def connect_db(db):
    return sqlite3.connect(db)

def init_db(db, sql):
    with closing(connect_db(db)) as db:
        with app.open_resource(sql) as f:
            db.cursor().executescript(f.read())
        db.commit()
        db.close()

def get_db(db):
    top = _app_ctx_stack.top
    if db:
        top.sqlite_db = sqlite3.connect(db)
    return top.sqlite_db

def update_db(db, query, request_form=()):
    #print('querty',query)
    #print('requestform',request_form)
    
    
    db = get_db(db)
    
    msg = 'success'
    try:
        ret = db.execute(query, request_form)
        #print("success execute")
        db.commit()
    except sqlite3.Error as er:
        #print(er.args[0])
        
        #print("rollback")        
        msg = 'rollback'
        db.rollback()
    
    #print("closing db")
    db.close()

    return msg

def query_db(db, query, args=(), oneline=False, line_num=0):
    
    cur = get_db(db).execute(query, args)    
    rv = cur.fetchall()
    cur.close()
    return (rv[line_num] if rv else None) if oneline else rv
    
def select_query(table_name, selection='*'):
    return 'select ' + selection + ' from ' + table_name
    
def selection_query(table_name, selection, where_var):
    return 'select ' + selection + ' from ' + table_name +' where ' + where_var

def selection_query_two(table_name, selection, where_var, where_var2):
    return 'select ' + selection + ' from ' + table_name +' where ' + where_var + ' and ' + where_var2

def selection_query_order(table_name, selection, order):
    return 'select ' + selection + ' from ' + table_name +' order by ' + order + ' desc '

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

def update_query2(table_name, set_vars, where_var, where_var2):
    query = 'update ' + table_name + ' set '    
    query += (set_vars + ' = ?')        
    query += ' where '     
    query += where_var + ' = ? and ' + where_var2 + ' = ? '
    return query

def insert_query(table_name, insert_vars, n):
    return 'insert into '+ table_name + ' ' + insert_vars + ' values ( ' + '?, '*(n-1) + '?)'

def insert_query_test(table_name, vars):
    return 'insert into '+ table_name + 'values (' + vars + ')'	
#####
def get_name(path):
  conn = sqlite3.connect('this_company.db')
  cur = conn.cursor()
  
  A = cur.execute("select * from THIS_COMPANY")
  B = A.fetchall()
  #print(B)
  #po = cur.execute("select name from sqlite_master WHERE type='table';")
  #po = cur.fetchall()
  #colname = cur.execute("select sql from sqlite_master where name='"+po[0][0]+"'")
  #colname = cur.fetchall()
  #print('table_name: ',po[0][0])
  #print('column_name: ',colname)
  #pp(colname)
  conn.close()
  

#order_no = query_db('this_company.db', insert_query_test('THIS_COMPANY',"'A','B','C','D','E','F'"))

def delete_query(table_name, where_var):
    return 'delete from ' + table_name + ' where ' + where_var + ' =?'

def delete_query_two(table_name, where_var1, where_var2):
    return 'delete from ' + table_name + ' where ' + where_var1 + ' and '+ where_var2

