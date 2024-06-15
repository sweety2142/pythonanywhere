#-*- coding: utf-8 -*-
from flask import Blueprint, render_template, abort, make_response, flash, request, jsonify, redirect, url_for, session
from jinja2 import TemplateNotFound
from dv.config import Cfg
from collections import defaultdict
from datetime import datetime, timedelta
import pprint as pp

from dv.database import *

USER_LIST = Cfg.USER_PATH
LOG_FILE = Cfg.LOG_FILE
LOG_ACTIVITY = Cfg.LOG_ACTIVITY

#create blueprint
admin_bp = Blueprint('admin', __name__)
users_bp = Blueprint('users',__name__)
dashboards_bp = Blueprint('dashboards',__name__)

def record_logging(path, ip, uid, action, data):
    with open(path, 'a+',encoding='utf-8') as fh:
        logging = datetime.today().strftime("%Y-%m-%d %H:%M:%S")+' (DB) '+action+' : '
        if uid:
            logging+=uid+' '
        logging += ip+' '+data+'\n'
        fh.write(logging)
        
def read_logs(file_name):
  logs = ''
  with open(file_name,'r',encoding='utf-8') as f:
    logs=[it.split() for it in f]
        #logs = [l.split() for l in it]

  return logs
  
@admin_bp.route('/admin/',methods=['POST','GET'])
def admin():
  try:
    total = dict()
    logs = read_logs(LOG_FILE)
    total['users']=len(query_db(USER_LIST, select_query('user_list')))
    total['views']=len(['' for item in logs if item[3] and item[3]=="IN"])

    #total['cals']=len(['' for l in logs if l[3][:-1] == 'DO'])
    record_logging(LOG_FILE, request.remote_addr, 'ADM', 'ADMIN','query admin page')
    AD ='check'
    return render_template('admin_home.html', total=total, AD=AD)
  except TemplateNotFound:
    abort(404)
    
@users_bp.route('/users/', methods=['POST','GET'])
def users():
  try:
    if request.method == 'GET' and 'index' in request.args:
      user_idx = request.args.get('index')
      print(user_idx)
      qdb_one = query_db(USER_LIST, select_query('user_list'), oneline=True, line_num=int(user_idx)-1)
      qdb_dict = dict(num=qdb_one[0], name=qdb_one[1], mail=qdb_one[2],password=qdb_one[3],creation_date=qdb_one[4], authority=qdb_one[6])
      print(qdb_dict)
      return jsonify(qdb_dict)
    qdb_user = query_db(USER_LIST, select_query('user_list'))
    users = [ dict(num=row[0], name=row[1], password=row[3], mail=row[2], creation_date=row[4], authority=row[6]) for row in qdb_user ]
    print(users)

    return render_template('users.html', user_list=users, AD='check')
  except TemplateNotFound:
    abort(404)
    
@users_bp.route('/users/edit/', methods=['POST'])
def edit():
  try:
    if request.method == 'POST':
      num = request.json['num']
      pw = request.json['pw']
      name=request.json['name']
      mail=request.json['mail']
      authority=request.json['authority']

      update_db(USER_LIST, update_query('user_list',['name','mail','password','authority'],'num'),[name,mail,pw,authority,num])      
    return redirect(url_for('users.users'))
  except TemplateNotFound:
    abort(404)
    
@users_bp.route('/users/delete', methods=['POST'])
def delete():
  try:
    if request.method == 'POST':
      idx = request.json['index']
      update_db(USER_LIST, delete_query('user_list','num'),[idx])
      print("ss-")
    return redirect(url_for('users.users'))
  except TemplateNotFound:
    abort(404)
    
    
