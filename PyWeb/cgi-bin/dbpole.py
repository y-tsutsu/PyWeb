# coding: utf-8

import sqlite3, os
from httphandler import Request, Response, get_htmltemplate
import cgitb; cgitb.enable()

form_body = """
    <form method="post" action="/cgi-bin/dbpole.py">
        好きな軽量言語は？<br />
        {0}
        <input type="submit" />
    </form>"""

radio_partu = """
<input type="radio" name="language" value="{0}" />{1}
<div style="border-left: solid {2}em lime; ">{3}</div>
"""

def incrementvalue(cur, lang_name):
    cur.execute("""SELECT value FROM language_pole
                   WHERE name = '{0}'""".format(lang_name))

    item = None
    for item in cur.fetchall():
        cur.execute("""UPDATE language_pole
                       SET value = {0} WHERE name = '{1}'""".format(item[0] + 1, lang_name))

    if not item:
        cur.execute("""INSERT INTO language_pole(name, value)
                       VALUES('{0}', 1)""".format(lang_name))

con = sqlite3.connect("./dbfile.dat")
cur = con.cursor()

try:
    cur.execute("""CREATE TABLE language_pole(
                   name text, value int);""")
except:
    pass

req = Request()
if "language" in req.form:
    incrementvalue(cur, req.form["language"].value)

lang_dic = {}
cur.execute("""SELECT name, value FROM language_pole;""")
for res in cur.fetchall():
    lang_dic[res[0]] = res[1]

content = ""
for lang in ["Perl", "PHP", "Python", "Ruby"]:
    num = lang_dic.get(lang, 0)
    content += radio_partu.format(lang, lang, num, num)

con.commit()

res = Response()
body = form_body.format(content)
res.set_body(get_htmltemplate("軽量言語アンケート DB版").format(body))
print(res)
