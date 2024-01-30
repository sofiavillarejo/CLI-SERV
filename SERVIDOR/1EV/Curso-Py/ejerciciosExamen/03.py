#!/Library/Frameworks/Python.framework/Versions/3.12/bin/python3
print("Content-type: text/html\n")

preciosProductosID = {
    "CA132":99.2,
    "CB231":55.7,
    "CA332": 101.0,
    "CD563":65.2,
    "CB838":48.1
}
# print(preciosProductosID.keys())
# print(preciosProductosID.values())

########################################TABLA######################
# print("<table>")
# for datos in preciosProductosID.items():
#     print("<th>Identificador</th>")
#     print("<th>Precio</th>")
#     print(f"<tr><td>{datos[0]}</td><td>{datos[1]}</td></tr>")

# # total = 0
# # for num in preciosProductosID.values():   
# #         total +=num

# total = sum(preciosProductosID.values())

# print("<th colspan='2'>Total</th>")
# print(f"<tr><td style='color:blue;text-align:center;'>{total}</td></tr>")
# print("</table>")

######################################LISTA######################
print("<ul>")
for prod in preciosProductosID.values():
    print(f"<li>{prod}</li>")
print("</ul>")