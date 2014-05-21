# coding: utf-8

import cgi
import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding = "utf-8")

print("Content-type: text/html\n")
print(cgi.print_environ())
