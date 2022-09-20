import csv

provincia = "Cartago"
cantones = ["Cartago", "El Guarco", "La Unión", "Oreamuno"]

lines = open("PYMES_activas_junio_2022.csv", "r", encoding="iso-8859-1")
data = csv.reader(lines, delimiter=';')
archivo_filtrado = open("PYME_filtrada.csv", "w")
writer = csv.writer(archivo_filtrado)
for line in data:
    if (line[6] == provincia) and (line[5] == "Micro" or line[5] == "Pequeña") and (line[7] in 
    cantones) and (line[9] == "Industria Manufacturera"):
        writer.writerow(line)

