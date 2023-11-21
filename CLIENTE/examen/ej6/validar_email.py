#!C:\Users\zx22student3329\AppData\Local\Programs\Python\Python311\python.exe

import cgi, json, re
form = cgi.FieldStorage()
email = form['email'].value

regex = r'^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
resultado = re.match(regex, email) is not None
print("Content-type: text/plain\n")
print(json.dumps(resultado))