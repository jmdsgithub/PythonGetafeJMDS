print("Diccionarios Python")

provincias = dict()

provincias = {    924 : "Badajoz",    956:  "Cádiz",    958 : "Granada",    959 : "Huelva",    91 : "Madrid",    95 : "Málaga",    968 : "Murcia",    923 : "Salamanca",    95 : "Sevilla",    922 : "Sta. Cruz de Tenerife",    975 : "Soria",    96 : "Valencia",    976 : "Zaragoza"}

print(provincias)

print("Número de provincias: ",len(provincias))


dato=provincias.get(91)
print("La clave 91 corresponde al valor: ", dato)
