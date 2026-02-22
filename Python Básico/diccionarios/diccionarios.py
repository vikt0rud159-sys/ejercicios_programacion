name = input("Nombre del hotel: ")
stars = input("Numero de strellas: ")
room_num1 = input ("Numero de habitación: ")
floor1 = input("Numero de piso: ")
price1 = input("Precio por noche: ")
room_num2 = input ("Numero de habitación: ")
floor2 = input("Numero de piso: ")
price2 = input("Precio por noche: ")

hotel_inf ={
		"hotel name": name,
		"stars": stars,
		"rooms": {
			"room1" : room_num1,
			"floor room1" : floor1,
			"price room1" : price1,
            "room2" : room_num2,
            "floor room2" : floor2,
            "price room2" : price2
		},
	},

print(hotel_inf)