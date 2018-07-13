#!/data1/daihao/myproject/venv/bin/python

import cgi, cgitb
from template import *

form1 = cgi.FieldStorage()

num1 = form1.getvalue("num1")
num2 = form1.getvalue("num2")
num3 = None

if not num1 is None and not num2 is None:
    num1 = int(num1)
    num2 = int(num2)
    num3 = num1 + num2


print(start_response())
print(start_div("center", "margin-top: 40px;"))
print(img("../views/a.png"))
print(end_div())


print(start_div("center", "margin-top: 60px;"))
print(start_form())
print(input_label("num1", "add1"))
print("+")
print(input_label("num2", "add2"))
print("=")
if num3 is None:
    print(input_label("num3", "result", "", "readonly"))
else:
    print(input_label("num3", "result", str(num3), "readonly"))
print(end_form())
print(end_div())