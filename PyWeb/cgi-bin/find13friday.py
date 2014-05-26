# coding: utf-8

import cgi
from datetime import datetime
import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding = "utf-8")

html_body = """
<html><head>
<meta http-equiv="content-type" content="text/html;charset=utf-8">
</head>
<body>
%s
</body>
</html>"""

content = ""

form = cgi.FieldStorage()
year_str = form.getvalue("year", "")
if not year_str.isdigit():
    content = "西暦を入力して下さい"
else:
    year = int(year_str)
    friday13 = 0
    for month in range(1, 13):
        date = datetime(year, month, 13)
        if date.weekday() == 4:
            friday13 += 1
            content += "%d年%d月13日は金曜日です" % (year, date.month)
            content += "<br />"

    if friday13:
        content += "%d年には合計%d個の13日の金曜日があります" % (year, friday13)
    else:
        content += "%d年には13日の金曜日がありません" % year


print("Content-type: text/html;charset=utf-8\n")
print(html_body % content)
