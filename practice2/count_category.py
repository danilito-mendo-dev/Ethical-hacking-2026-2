vulnerabilidades = list()

vulnerabilidades.append({"title": "SQL Injection", "owasp_category": "A03"})
vulnerabilidades.append({"title": "XSS", "owasp_category": "A03"})
vulnerabilidades.append({"title": "Broken Auth", "owasp_category": "A07"})
vulnerabilidades.append({"title": "SSRF", "owasp_category": "A10"})
vulnerabilidades.append({"title": "CSRF", "owasp_category": "A07"})

conteo = {}

for i in vulnerabilidades:
    categoria = i["owasp_category"]
    if categoria in conteo:
        conteo[categoria] += 1
    else:
        conteo[categoria] = 1

print(f"Conteo por categoría: {conteo}")