class Bus:
	def __init__ (self, max_passengers):
		self.max_passengers = max_passengers
		self.persons_in_bus = []
		
	def add_passenger(self, person):
		if len(self.persons_in_bus) >= self.max_passengers:
			print("\nAutobús lleno")
			return
		self.persons_in_bus.append(person)
		
	def subtract_person(self):
		self.persons_in_bus.pop(0)


def program():
    bus1 = Bus(3)
    bus1.add_passenger("Jose")
    bus1.add_passenger("Pablo")
    bus1.subtract_person()
    bus1.add_passenger("Lola")
    print(f"\n{bus1.persons_in_bus}\n")


program()