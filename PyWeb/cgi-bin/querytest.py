# coding: utf-8

html_body = """
<html><body>
foo = %s
</body></html>"""

import cgi
form = cgi.FieldStorage()

print("Content-type: text/html\n")
print(html_body % form.getvalue("foo", "N/A"))
