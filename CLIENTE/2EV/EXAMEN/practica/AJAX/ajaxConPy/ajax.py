#!C:\Users\Sofía\AppData\Local\Programs\Python\Python312\python.exe

import cgi, json, re

form = cgi.FieldStorage()
email = form['email'].value

regex = r'^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'

resultado = re.match(regex,email) is not None

print("Content-type: text/plain\n")
print(json.dumps(resultado))