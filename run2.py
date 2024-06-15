from flask import Flask,request, session, redirect, url_for, abort,render_template
import sqlite3

from dv import create_app
app=create_app()

if __name__ == '__main__':
    app.run(port=7776, use_reloader=True, debug=True, threaded=True, host='0.0.0.0')
