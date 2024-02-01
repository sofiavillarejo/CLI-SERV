#!/Library/Frameworks/Python.framework/Versions/3.12/bin/python3

print("Content-type: text/html\n")

for i in range (1,20):
    print(f"<div><img src='imagen/coche{i}.png' alt='imagen de coche {i}'/></div>")