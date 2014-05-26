# coding: utf-8

from rssparser import parse_rss
from httphandler import Request, Response, get_htmltemplate
import cgitb; cgitb.enable()

form_body = """
    <form method="post" action="/cgi-bin/rssreader1.py">
        RSSのURL：
        <input type="text" size="40" name="url" value="{0}" />
        <input type="submit" />
    </form>"""

rss_parts = """
<h3><a href="{link}">{title}</a></h3>
<p>{description}</p>
"""

content = "URLを入力してください"
req = Request()
if "url" in req.form:
    try:
        rss_list = parse_rss(req.form["url"].value)
        content = ""
        for d in rss_list:
            content += rss_parts.format(**d)
    except:
        pass

res = Response()
body = form_body.format(req.form.getvalue("url", ""))
body += content
res.set_body(get_htmltemplate("RSS リーダー").format(body))
print(res)
