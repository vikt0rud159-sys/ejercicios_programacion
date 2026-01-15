name = input("Ingrese su nombre:")
last_name = input("Ingrese su apellido:")
years = input("Ingrese su edad en años:")
years = int(years)
if(years>=65):
    print("Usted es adulto mayor")
elif(years>=30):
    print("Usted es adulto")
elif(years>=18):
    print("Usted es joven adulto")
elif(years>=12):
    print("Usted es adolescente")
elif(years>=9):
    print("Usted es preadolescente")
elif(years>=4):
    print("Usted es niño")
elif(years>=0):
    print("Usted es bebé")  
