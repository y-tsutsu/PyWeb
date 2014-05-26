# coding: utf-8

import sqlite3
from string import Template
from os import path
from httphandler import Request, Response, get_htmltemplate
import cgitb; cgitb.enable()
import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding = "utf-8")

con = sqlite3.connect("./bookmark.dat")
cur = con.cursor()
try:
    cur.execute("""CREATE TABLE bookmark (title text, url text)""")
except:
    pass

req = Request()
f = req.form
value_dic = {"message":"", "title":"", "url":"", "bookmarks":"", "headtitle":"簡易ブックマーク"}

if "post" in f:
    if not f.getvalue("title", "") or not f.getvalue("url", ""):
        value_dic["message"] = "タイトルとURLは必須項目です"
        value_dic["title"] = f.getvalue("title", "")
        value_dic["url"] = f.getvalue("url", "")
    else:
        cur.execute("""INSERT INTO bookmark(title, url) VALUES(?, ?)""",
                    (f.getvalue("title", ""), f.getvalue("url", "")))
        con.commit()

res = Response()
with open(path.join(path.dirname(__file__), "bookmarkform.html"), encoding = "utf-8") as f:
    t = Template(f.read())
body = t.substitute(value_dic)
res.set_body(body)
print(res)
