# coding: utf-8

import cgi
import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding = "utf-8")

html_body = """
<html>
<head>
<meta http-equiv="content-type" content="text/html;charset=utf-8" />
</head>
<body>
{0}
</body>
</html>
"""

form = cgi.FieldStorage()
content=""
for i, item in enumerate(form.getlist("language")):
    content += "{0} : {1} <br />".format(i + 1, item)

print("Content-type: text/html\n")
print(html_body.format(content))
