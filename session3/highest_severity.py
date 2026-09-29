#Ordena una lista de diccionarios de vulnerabilidades por un campo numérico 'severity', de mayor a menor, usando sorted().

vulnerabilities = list()

vulnerabilities.append({"nombre": "SQL Injection", "severity": 9})
vulnerabilities.append({"nombre": "Cross-Site Scripting", "severity": 7})
vulnerabilities.append({"nombre": "Remote Code Execution", "severity": 5})
vulnerabilities.append({"nombre": "Cross-Site Request Forgery", "severity": 3})

vulnerabilities_ordenadas = sorted(
    vulnerabilities, 
    key=lambda v:v["severity"], 
    reverse=True
)

print("Vulnerabilidades ordenadas por severidad (mayor a menor):\n")
for v in vulnerabilities_ordenadas:
    print(f"Severidad {v['severity']:>2} - {v['nombre']}")