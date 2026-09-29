ports = list()

ports.append({"port": 22, "status": "open"})
ports.append({"port": 80, "status": "open"})
ports.append({"port": 443, "status": "open"})
ports.append({"port": 21, "status": "closed"})
ports.append({"port": 23, "status": "closed"})

counter = list()

for i in ports:
    if i["status"] == "open":
        print(f"Puerto: {i['port']}, Estado: {i['status']}")
        counter.append(i)

print(f"Puertos abiertos: {len(counter)}")