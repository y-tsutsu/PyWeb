# coding: utf-8

import pickle, os
from httphandler import Request, Response, get_htmltemplate
import cgitb; cgitb.enable()

form_body = """
    <form method="post" action="/cgi-bin/picklepole.py">
        好きな軽量言語は？<br />
        {0}
        <input type="submit" />
    </form>"""

radio_partu = """
<input type="radio" name="language" value="{0}" />{1}
<div style="border-left: solid {2}em skyblue; ">{3}</div>
"""

lang_dic = {}
fpath = "./favorite_language.dat"
if os.path.exists(fpath):
    with open(fpath, "rb") as f:
        lang_dic = pickle.load(f)

req = Request()
if "language" in req.form:
    lang = req.form["language"].value
    lang_dic[lang] = lang_dic.get(lang, 0) + 1

f = open(fpath, "wb")
pickle.dump(lang_dic, f)

content = ""
for lang in ["Perl", "PHP", "Python", "Ruby"]:
    num = lang_dic.get(lang, 0)
    content += radio_partu.format(lang, lang, num, num)

res = Response()
body = form_body.format(content)
res.set_body(get_htmltemplate("軽量言語アンケート").format(body))
print(res)
