#!/data1/daihao/myproject/venv/bin/python

import cgi, cgitb
from template import *

form1 = cgi.FieldStorage()

name = form1.getvalue("name")


print ("Content-type: text/html \n\n")
print (img("../views/a.png"))