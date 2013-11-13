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
%s
</body>
</html>"""

form = cgi.FieldStorage()
body_line = []
body = form.getvalue("body", "")

for cnt in range(0, len(body), 10):
    line = body[:10]
    line += "".join([" " for i in range(len(line), 10)])
    body_line.append(line)
    body = body[10:]

body_line_v = [" ".join(reversed(x)) for x in zip(*body_line)]

print("Content-type: text/html;charset=utf-8\n")
print(html_body % "<br />".join(body_line_v))
